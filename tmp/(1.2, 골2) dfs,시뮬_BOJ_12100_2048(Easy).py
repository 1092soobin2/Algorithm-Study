# (1, 골2) BOJ_12100_2048(Easy)

# === input ===
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# === algorithm ===
EMPTY = 0
DIRECTION_LIST = [[-1, 0], [0, -1], [1, 0], [0, 1]]


# 0, 1, 2, 3 위, 왼, 아, 오
def move_up_down(up: bool):
    global board

    if up:
        range_r = range(N)
        delta_r = 1
    else:
        range_r = range(N - 1, -1, -1)
        delta_r = -1

    for c in range(N):
        prev_r = range_r[0]
        for r in range_r:
            # 공이 있는 경우
            if board[r][c] != EMPTY:
                # 제일 아래 칸에 있는 경우
                if prev_r == r:
                    continue
                # 이동
                if board[prev_r][c] == EMPTY:
                    board[prev_r][c] = board[r][c]
                    board[r][c] = EMPTY
                # 합쳐짐
                elif board[prev_r][c] == board[r][c]:
                    board[prev_r][c] += board[r][c]
                    board[r][c] = EMPTY
                    prev_r += delta_r
                # 윗 칸으로 이동
                else:
                    board[prev_r + delta_r][c] = board[r][c]
                    if prev_r + delta_r != r:
                        board[r][c] = EMPTY
                    prev_r += delta_r

    print_debug(f"move_up_down({'up' if up else 'down'})")


def move_left_right(left: bool):
    global board

    if left:
        range_c = range(N)
        delta_c = 1
    else:
        range_c = range(N - 1, -1, -1)
        delta_c = -1

    for r in range(N):
        prev_c = range_c[0]
        for c in range_c:
            if prev_c == c:
                continue
            if board[r][c] != EMPTY:
                if board[r][prev_c] == EMPTY:
                    board[r][prev_c] = board[r][c]
                    board[r][c] = EMPTY
                elif board[r][prev_c] == board[r][c]:
                    board[r][prev_c] += board[r][c]
                    board[r][c] = EMPTY
                    prev_c += delta_c
                else:
                    board[r][prev_c + delta_c] = board[r][c]
                    if c != prev_c + delta_c:
                        board[r][c] = EMPTY
                    prev_c += delta_c
    print_debug(f"move_left_right({'left' if left else 'right'})")


def dfs(acc: int):
    global board

    if acc == 5:
        return max(map(max, board))

    backup_board = [board[r][:] for r in range(N)]
    ret_int = 0

    print_debug(f"{acc}", False)
    move_up_down(True)
    ret_int = max(ret_int, dfs(acc + 1))
    board = [backup_board[r][:] for r in range(N)]

    print_debug(f"{acc}", False)
    move_up_down(False)
    ret_int = max(ret_int, dfs(acc + 1))
    board = [backup_board[r][:] for r in range(N)]

    print_debug(f"{acc}", False)
    move_left_right(True)
    ret_int = max(ret_int, dfs(acc + 1))
    board = [backup_board[r][:] for r in range(N)]

    print_debug(f"{acc}", False)
    move_left_right(False)
    ret_int = max(ret_int, dfs(acc + 1))
    board = [backup_board[r][:] for r in range(N)]

    return ret_int


def print_debug(title="", arr=True):
    global board

    if not DEBUG:
        return

    print("===="*N)
    print(title)
    if arr:
        for r in range(N):
            for c in range(N):
                print(f"{board[r][c]:4}", end="")
            print()
        print("===="*N + "\n\n\n")


# === output ===
DEBUG = False
# DEBUG = True


# ans: 최대 5번 이동하여 만들 수 있는 max 블록의 값
print(dfs(0))
