# (1.2, 골2) 시뮬_Codetree_승자독식모노폴리

# n * n grid    [계약 번호, 남은 턴수]
# m player      [위치, 방향]


from collections import defaultdict

# === input ===
N, M, K = map(int, input().split())
player_dict = dict()
LOCATION, DIRECTION, PREFERENCE = 0, 1, 2
board = [[[0, 0] for _ in range(N)] for _ in range(N)]
CONTRACT_NUM, TURN = 0, 1


# === algorithm ===
# 자료 구조 초기화
def init():
    global player_dict, board

    # 격자 정보
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 초기 방향 정보
    direction_list = list(map(lambda x: int(x) - 1, input().split()))
    # 방향별 이동 우선 순위 (0 위, 1 아래, 2 왼, 3 오)
    preference_list = [[list(map(lambda x: int(x) - 1, input().split())) for _ in range(4)] for _ in range(M)]

    for r in range(N):
        for c in range(N):
            if grid[r][c] != 0:
                player_num = grid[r][c]
                player_dict[player_num] = [[r, c], direction_list[player_num - 1], preference_list[player_num - 1]]
                board[r][c] = [player_num, K]

    print_debug()


def one_turn():

    # 이동
    def move_all_player():
        global player_dict

        def move_one(player_num):

            direction_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            [r, c], d, prefer_list = player_dict[player_num]

            # 방향별 우선 순위대로 이동
            next_loc = [-1, -1]
            # 인접 칸 중 독점계약 X 칸
            for next_d in prefer_list[d]:
                dr, dc = direction_list[next_d]
                next_r, next_c = r + dr, c + dc
                if 0 <= next_r < N and 0 <= next_c < N and board[next_r][next_c][CONTRACT_NUM] == 0:
                    next_loc = [next_r, next_c]
                    break

            # 그러한 칸이 없으면, 본인 독점계약 칸
            if next_loc == [-1, -1]:
                for next_d in prefer_list[d]:
                    dr, dc = direction_list[next_d]
                    next_r, next_c = r + dr, c + dc
                    if 0 <= next_r < N and 0 <= next_c < N and board[next_r][next_c][CONTRACT_NUM] == player_num:
                        next_loc = [next_r, next_c]
                        break

            player_dict[player_num][LOCATION] = next_loc
            player_dict[player_num][DIRECTION] = next_d

        for p in player_dict:
            move_one(p)

    # 칸 이동 시 독점 계약 -> k 턴동안 유효
    def flow_one_second():
        global board

        for r in range(N):
            for c in range(N):
                # 유효 번호 있는 경우에 -1
                if board[r][c][TURN] > 0:
                    board[r][c][TURN] -= 1
                    # 1초가 지났을 떄 유효 턴이 끝나면 번호를 0으로 세팅
                    if board[r][c][TURN] == 0:
                        board[r][c][CONTRACT_NUM] = 0

    def move_in_board():
        global board

        loc_dict = defaultdict(list)

        # 모든 플레이어 이동
        for p in player_dict:
            loc_dict[tuple(player_dict[p][LOCATION])].append(p)

        # 모든 플레이어 이동 후, 한 칸에 여러 플레이어 -> 제일 작은 번호만 살아남는다.
        for loc_tup in loc_dict:
            loc_list = loc_dict[loc_tup]
            survivor = min(loc_list)
            if len(loc_list) > 1:
                for p in loc_list:
                    if p == survivor:
                        continue
                    del player_dict[p]
            nr, nc = loc_tup
            board[nr][nc] = [survivor, K]

    # player 다음 칸 정하기
    move_all_player()
    # board 에 시간 흐르기
    flow_one_second()
    # board 에 player 위치 업데이트 (K)
    move_in_board()
    print_debug()


def print_debug():
    if not DEBUG:
        return

    print("=====================================")
    print(f"player: {player_dict}")
    for r in range(N):
        print(*board[r])
    print("=====================================")


# === output ===
DEBUG = False
# DEBUG = True

init()

turn = 0
while len(player_dict) != 1:
    # 답이 1000을 넘거나 불가능한 경우에는 -1을 출력
    if turn >= 1000:
        turn = -1
        break
    turn += 1
    one_turn()
print(turn)
