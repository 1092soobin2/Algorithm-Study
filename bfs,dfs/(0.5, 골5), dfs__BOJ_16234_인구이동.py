
from collections import deque

# L <= (diff) <= R 이면
# 하루동안 연다
# 인접한 칸만을 이용해 이동

# ===input===
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


# ===algorithm===
def get_united():
    ret_united = []

    visited = [[False] * N for _ in range(N)]

    def dfs(start_r, start_c):

        ret_visited = []

        stack = [[start_r, start_c]]
        ret_visited.append([start_r, start_c])
        visited[start_r][start_c] = True

        while stack:
            curr_r, curr_c = stack.pop(0)

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r+dr, curr_c+dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if L <= abs(board[curr_r][curr_c] - board[nr][nc]) <= R:
                        stack.append([nr, nc])
                        ret_visited.append([nr, nc])
                        visited[nr][nc] = True

        return ret_visited

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                new_united = dfs(r, c)
                if len(new_united) > 1:
                    ret_united.append(new_united)

    return ret_united


def move_population():

    ret_num_moving = 0

    while True:
        united_list = get_united()
        if not united_list:
            return ret_num_moving

        # 인구 이동
        ret_num_moving += 1
        for united in united_list:
            population = sum(map(lambda x: board[x[0]][x[1]], united)) // len(united)
            for r, c in united:
                board[r][c] = population
            # print(united)
            # print(board)

    print("n/a")
    exit()


# ===output===
print(move_population())