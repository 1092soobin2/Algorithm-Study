# (2) 구현__Codetree_싸움땅 1.5
# 정보 분산으로(자료 구조가 달라서 쩔 수) 업데이트 시에 까먹음 -> 아예 업데이트 부분에 ;TODO 자료구조1 자료구조2; 이렇게 써놓자

# n x n board
# m palyer
# k round

# player (loc, stat, direction, gun=0, point=0)
    # initial stat
LOCATION = 0
STAT = 1
DIRECTION = 2
GUN = 3
POINT = 4
DIRECTION_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# gun (ability)

# one_round
# move_1_player를 모든 플레이어에게 시행


# ans: 최종 point


# ===input===
n, m, k = map(int, input().split())

gun_board = []      # 각 칸에 gun_list가 있다.
players = [[] for _ in range(m + 1)]
player_board = [[0]*n for _ in range(n)]
def get_inputs():
    global gun_board, players, player_board
    for _ in range(n):
        input_guns = list(map(int, input().split()))
        appended_guns = []
        # list로 바꿔줌
        for gun in input_guns:
            appended_guns.append([gun])
        gun_board.append(appended_guns)
    for player_id in range(1, m+1):
        x, y, d, s = map(int, input().split())
        players[player_id] = [(x-1, y-1), s, d, 0, 0]
        player_board[x-1][y-1] = player_id


# ===algorithm===
def print_arr_2d(arr, arr2=None, title='', edge=n) :
    print(title)
    print("=================")
    for r in range(edge):
        for c in range(edge):
            print(arr[r][c], end=' ')
        if arr2:
            print("\t\t", end="")
            for c in range(edge):
                print(arr2[r][c], end=' ')
        print()
    print("=================\n")


def move_one_player(one_player: list):          # players의 요소가 인자로 주어짐

    def move_and_pop_player_id(player) -> int:
        # move
        (curr_r, curr_c), _, direction, _, _ = player

        # 1) 자신의 방향으로 이동
        dr, dc = DIRECTION_LIST[direction]
        # 2) 격자를 벗어나는 경우 -> 정반대 방향으로 이동
        if not(0 <= curr_r+dr < n and 0 <= curr_c+dc < n):
            player[DIRECTION] = (direction + 2) % 4
            dr, dc = DIRECTION_LIST[player[DIRECTION]]
        player[LOCATION] = (curr_r+dr, curr_c+dc)

        # pop
        popped_id = player_board[curr_r][curr_c]
        player_board[curr_r][curr_c] = 0
        return popped_id

    def get_gun(player):
        (curr_r, curr_c), _, _, gun, _ = player
        if not gun_board[curr_r][curr_c]:
            return

        # 1-1) 총을 가지지 않을 경우 -> 총이 있으면 획득
        if gun == 0:
            gun_board[curr_r][curr_c].sort()
            player[GUN] = gun_board[curr_r][curr_c].pop()
        # 1-2) 총을 가진 경우 -> 더 쎈 총 하나만 가질 수 있음, 원래 총은 격자에 내려 두기
        else:
            gun_board[curr_r][curr_c].sort()
            if gun_board[curr_r][curr_c][-1] > gun:
                # 더 쏀 총 갖기
                player[GUN] = gun_board[curr_r][curr_c].pop()
                # 내려 두기
                gun_board[curr_r][curr_c].append(gun)

    def no_fight(player1, player1_id):
        get_gun(player1)
        tr, tc = player1[LOCATION]
        player_board[tr][tc] = player1_id

    # sum(stat+gun) 더 큰 player 승리 (같으면 초기 능력치 큰 player 승리
    def fight(player1, player_id1):
        (r1, c1), stat1, _, gun1, _ = player1
        _, stat2, _, gun2, _ = player2 = players[player_board[r1][c1]]

        # 1) 승리자, 패배자 결정
        score, score2 = stat1+gun1, stat2+gun2
        winner, loser = player1, player2
        winner_id, loser_id = player_id1, player_board[r1][c1]
        if score < score2 or (score == score2 and stat1 < stat2):
            winner, loser = loser, winner
            winner_id, loser_id = loser_id, winner_id
        # print(f"fight! Winner is {winner_id}, loser is {loser_id}")

        # 2-1) 패배자
        # -가진 총을 격자에 내려놓고
        gun_board[loser[LOCATION][0]][loser[LOCATION][1]].append(loser[GUN])
        loser[GUN] = 0
        # -direction으로 1칸 이동
        # -player O || out of space -> clockwise 90
        for clockwise in range(4):
            next_d = (loser[DIRECTION] + clockwise) % 4
            curr_r, curr_c = loser[LOCATION]
            dr, dc = DIRECTION_LIST[next_d]
            next_r, next_c = curr_r+dr, curr_c+dc
            if (0 <= next_r < n and 0 <= next_c < n) and player_board[next_r][next_c] == 0:
                loser[LOCATION] = (next_r, next_c)
                loser[DIRECTION] = next_d
                get_gun(loser)
                break

        # 2-2) 승리자: sum의 차이만큼 포인트로 획득
        winner[POINT] += abs(score - score2)
        get_gun(winner)

        # 3) update player_board
        tr, tc = winner[LOCATION]
        player_board[tr][tc] = winner_id
        tr, tc = loser[LOCATION]
        player_board[tr][tc] = loser_id


    # 1. move player
    player_id = move_and_pop_player_id(one_player)
    r, c = one_player[LOCATION]
    # 2. in moved space
    # 1) player X
    if player_board[r][c] == 0:
        no_fight(one_player, player_id)
    # 2) player O
    else:
        fight(one_player, player_id)


def one_round():
    for player_id in range(1, m+1):
        move_one_player(players[player_id])


# ===output===
get_inputs()
for _ in range(k):
    one_round()
    # print(players)
    # print_arr_2d(player_board, gun_board)
ans = []
for pid in range(1, m+1):
    ans.append(players[pid][POINT])
print(*ans)