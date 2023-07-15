# (1, 골2) __BOJ_17837_새로운게임2


# N * N board [WHITE, RED, BLUE]
# K player  ID :[direction, 위치, up_player_id]
# 4개 이상 쌓이면 종료

# one turn: 1-K번 말을 순서대로 이동시키기
# 쌓여져있는 말을 함꼐 이동한다.
# -> 위치 별로 관리하기


# === input ===
N, K = map(int, input().split())
color_board = [list(map(int, input().split())) for _ in range(N)]
player_dict = dict()                            # ID :[direction, 위치]

WHITE, RED, BLUE = 0, 1, 2
DIRECTION_LIST = [[-1, 0], [0, -1], [1, 0], [0, 1]]
DIRECTION, LOCATION = 0, 1
player_board = [[list() for _ in range(N)] for _ in range(N)]      # player 수 관리


# player_dict 초기화
def init():
    global player_dict

    for k in range(K):
        r, c, d = map(lambda x : int(x) - 1, input().split())
        if d == 0:      # 오
            d = 3
        elif d == 1:    # 왼
            d = 1
        elif d == 2:    # 위
            d = 0
        elif d == 3:    # 아
            d = 2

        player_dict[k] = [d, [r, c]]
        player_board[r][c].append(k)

    print_debug("init() done.")


# === algorithm ===
# 한 말의 이동
def move(player_id: int):
    global player_dict, player_board

    def get_next_location():
        d, [tr, tc] = player_dict[player_id]
        dr, dc = DIRECTION_LIST[d]
        return tr + dr, tc + dc

    # 다음 칸 구하기
    nr, nc = get_next_location()

    # 다음 칸 BLUE || 경계 밖
    if not (0 <= nr < N and 0 <= nc < N) or color_board[nr][nc] == BLUE:
        player_dict[player_id][DIRECTION] = (player_dict[player_id][DIRECTION] + 2) % 4
        nr, nc = get_next_location()
        if not (0 <= nr < N and 0 <= nc < N) or color_board[nr][nc] == BLUE:
            return

    r, c = player_dict[player_id][LOCATION]
    player_idx = player_board[r][c].index(player_id)

    # 이동
    moving_player = player_board[r][c][player_idx:]
    player_board[r][c] = player_board[r][c][:player_idx]
    for pid in moving_player:
        player_dict[pid][LOCATION] = [nr, nc]

    # 다음 칸 WHITE
    if color_board[nr][nc] == WHITE:
        # player_board[nr][nc] += moving_player
        player_board[nr][nc].extend(moving_player)
    # 다음 칸 RED
    elif color_board[nr][nc] == RED:
        # 이동한 후, 그 위의 말들과 순서를 반대로 바꾼다.
        player_board[nr][nc].extend(reversed(moving_player))
        # player_board[nr][nc] += moving_player[::-1]
    else:
        print("in move(player_id : int): n/a color")

    print_debug(f"move({player_id}) done.")


# 한 턴
# return: True -> 종료되지 않은 채 한 턴이 끝남, False -> 게임이 종료됨.
def one_turn() -> bool:

    for player_id in range(K):
        move(player_id)
        # 종료 조건(이동한 칸에 말 개수 4개 이상) 확인
        r, c = player_dict[player_id][LOCATION]
        if len(player_board[r][c]) >= 4:
            return False
    return True


# 게임
# return: 게임 종료 턴 번호, >1000 이면 -1
def solution():

    init()
    turn = 1
    while turn <= 1000:
        if one_turn():
            turn += 1
        else:
            return turn
    return -1


def print_debug(title=""):
    if not DEBUG:
        return
    print("=========================")
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{str(player_board[r][c]):10}", end="")
        print()
    print("=========================")


# === output ===
DEBUG = False
print(solution())
