# (N/A, 골4) BOJ_9664_N-Queen

import sys

N = int(sys.stdin.readline())
answer = 0
visited = [[False]*N for _ in range(N)]

row = [-1] * N
col = [-1] * N


# 현재 퀸 자리 체크
def check_col(queen_row):
    if col[row[queen_row]] != -1:
        return False

    for r in range(queen_row):
        if abs(r - queen_row) == abs(row[r] - row[queen_row]):
            return False
    return True


def dfs(queen_row):
    global answer
    if queen_row == N:
        answer += 1
        return

    for queen_col in range(N):
        row[queen_row] = queen_col
        if check_col(queen_row):
            col[queen_col] = queen_row
            dfs(queen_row + 1)
            col[queen_col] = -1


# dfs(0)

for queen_col0 in range(N // 2):
    row[0] = queen_col0
    col[queen_col0] = 0
    dfs(1)
    col[queen_col0] = -1

answer *= 2

if N % 2 != 0:
    row[0] = N // 2
    col[N // 2] = 0
    dfs(1)
    col[N // 2] = -1

print(answer)
