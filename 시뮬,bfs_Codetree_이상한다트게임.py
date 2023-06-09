# (1, 골3) Codetree_이상한다트게임

# r 번째 원판(반지름 r)
# 각 원판에 m개의 점수  [[0, 1, 2, ... m-1] [0, 1, 2, ...m-1]

# === input ===
N, M, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotate_list = [list(map(int, input().split())) for _ in range(Q)]
CLOCKWISE, COUNTER_CLOCKWISE = 0, 1


# === algorithm ===

# 독립적 회전 (x, d, k)
def rotate_board(board_number, direction, speed):

    def rotate_one_board(board_i):
        global board

        if direction == CLOCKWISE:
            board[board_i] = board[board_i][-speed:] + board[board_i][:M - speed]
        elif direction == COUNTER_CLOCKWISE:
            board[board_i] = board[board_i][speed:] + board[board_i][:speed]
        else:
            print("n/a direction in rotate")

    # d: (시계 0/반시계 1)
    # 시계: 1 -> 1 + k
    # 반시계: m -> m - k
    for i in range(N):
        if (i + 1) % board_number == 0:
            rotate_one_board(i)

    print_debug(f"rotate{x, d, k} done")


# 회전 이후, 인접한 같은 수를 지운다.
def remove_number() -> bool:
    global board

    ret_bool = False

    def bfs(start: list):
        # 같은 숫자 집합 찾기
        queue = [start]
        visited = {tuple(start)}
        number = board[start[0]][start[1]]
        while queue:
            curr_r, curr_c = queue.pop(0)
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, (curr_c + dc) % M
                if 0 <= nr < N and (nr, nc) not in visited and board[nr][nc] == number:
                    queue.append([nr, nc])
                    visited.add((nr, nc))

        # 인접한 같은 숫자 제거
        if len(visited) > 1:
            for tr, tc in list(visited):
                board[tr][tc] = None
            return True

        return False

    # if board[r][c]: bfs() TODO: None인 경우 있음
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                ret_bool |= bfs([r, c])

    print_debug(f"remove done, result:{ret_bool}")

    return ret_bool


# 지워지는 수가 없는 경우 -> 원판 전체 수의 평균을 구해서 정규화.
def normalize():
    global board

    # 평균 구하기
    sum_num, len_num = 0, 0
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                sum_num += board[r][c]
                len_num += 1

    if len_num == 0:
        return

    avg = int(sum_num / len_num)

    # 정규화 : > 평균 -> -1, < 평균 + 1
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                if board[r][c] > avg:
                    board[r][c] -= 1
                elif board[r][c] < avg:
                    board[r][c] += 1

    print_debug("normalize done")


def get_sum():
    ret_int = 0
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                ret_int += board[r][c]
    return ret_int


def print_debug(title=""):
    if not debug:
        return

    print("===="*M)
    print(title)
    for r in range(N):
        for c in range(M):
            char = board[r][c] if board[r][c] else "   _"
            print(f"{char:4}", end="")
        print()
    print("===="*M)


# === output ===
debug = False
for x, d, k in rotate_list:
    rotate_board(x, d, k)
    if not remove_number():
        normalize()
print(get_sum())
