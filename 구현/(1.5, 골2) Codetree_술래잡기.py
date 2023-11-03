# 20:14~

# 4*4 grid

# 술래 1
    # [0, 0]
    # 한 번에 여러 칸 이동 可
    # 도둑말로 이동할 때, 지나는 칸의 말들은 잡지 않는다.
    # 도둑말이 없는 것으로 이동 不可
    # 이동 가능한 곳에 도둑말이 존재하지 않으면 게임을 끝낸다.
# player [방향, ]
    # 작은 순서대로 이동함.
    # 빈칸, 다른 도둑말이 있는 칸으로 이동 可
    # 이동할 수 있을 때까지 45도 반시계 회전
    # 이동할 수 없다면 이동하지 안흔ㄴ다.
    # 이동 칸에 도둑말이 있다면 해당 말과 위치를 바꾼다

import heapq
import copy


DIRECTION_LIST = [[-1, 1], [-1, 0], [-1, -1], [0, -1],
                    [1, -1], [1, 0], [1, 1], [0, 1]]        # counter-clockwise
LEN_EDGE = 4
PLAYER_ID, D_ID = 0, 1  # fo access of player
LOC, SCORE = 0, 2                 # for access of sullae

def move_all_player(board, sullae):

    player_list = [None]*(LEN_EDGE * LEN_EDGE + 1)

    for r in range(LEN_EDGE):
        for c in range(LEN_EDGE):
            if board[r][c]:
                player_list[board[r][c][PLAYER_ID]] = [r ,c]
    
    for player in player_list:
        if not player:
            continue
        [r, c] = player
        d_id = board[r][c][D_ID]

        while True:
            dr, dc = DIRECTION_LIST[d_id]
            nr, nc = r+dr, c+dc
            if 0 <= nr < LEN_EDGE and 0 <= nc < LEN_EDGE and [nr, nc] != sullae[LOC]:
                board[r][c][D_ID] = d_id
                if board[nr][nc]:
                    player_list[board[nr][nc][PLAYER_ID]] = [r, c]
                board[nr][nc], board[r][c] = board[r][c], board[nr][nc]
                break
            d_id = (d_id + 1) % 8
            if d_id == board[r][c][D_ID]:
                break
  #  print_debug(board, sullae, title="move_all")
    


def print_debug(board, sullae=None, title=""):
    if not DEBUG:
        return
    
    print("======================")
    print(title, sullae)

    for r in range(len(board)):
        for c in range(len(board[0])):
            print(f"{board[r][c]}", end="")
        print()
    print("======================")


def get_next_loc(board, sullae):
    next_sullae_loc = []

    dr, dc = DIRECTION_LIST[sullae[D_ID]]
    for i in range(1, LEN_EDGE):
        nr, nc = sullae[LOC][0] + dr * i, sullae[LOC][1] + dc * i
        if not ( 0 <= nr < LEN_EDGE and 0 <= nc < LEN_EDGE):
            break
        else:
            if board[nr][nc]:
                next_sullae_loc.append([nr, nc])

    return next_sullae_loc


def dfs(board, sullae):
    global answer

    move_all_player(board, sullae)

    next_loc = get_next_loc(board, sullae)
    if not next_loc:
        answer = max(answer, sullae[SCORE])
        return

    for r, c in next_loc:
        sullae_cp = [[r, c], board[r][c][D_ID], sullae[SCORE] + board[r][c][PLAYER_ID]]
        board_cp = copy.deepcopy(board)
        board_cp[r][c].clear()

        dfs(board_cp, sullae_cp)


answer = 0


def solution():
    input_board = [list(map(int, input().split())) for _ in range(LEN_EDGE)]
    board = []

    for r in range(LEN_EDGE):
        board.append([[input_board[r][2* i], input_board[r][2*i + 1] % 8] for i in range(LEN_EDGE)])

    sullae = [[0, 0], board[0][0][D_ID], board[0][0][PLAYER_ID]]
    board[0][0].clear()

    dfs(board, sullae)

    return answer
        

DEBUG = False

print(solution())
