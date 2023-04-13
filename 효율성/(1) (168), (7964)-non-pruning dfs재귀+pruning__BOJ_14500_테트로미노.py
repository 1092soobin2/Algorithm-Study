# (1) (168) dfs재귀+pruning__BOJ_14500_테트로미노

# 점수판이 주어짐.
# 점수판에 테트로미노를 적절히 놓아서 수들의 합이 최대가 되도록
# 회전, 대칭 가능

# ===input===
N, M = map(int, input().split())
score_board = [list(map(int, input().split())) for _ in range(N)]
max_score = max(map(max, score_board))


# ===algorithm===
def print_board(arr):
    print("===========")
    for r in range(N):
        for c in range(M):
            print(arr[r][c], end=' ')
        print()
    print("===========")


def sol():
    def dfs(arr, curr_r, curr_c, count, score):
        global ans

        # stop
        if score + (4 - count) * max_score < ans:
            # print(f"count: {count}, curr:{curr_r, curr_c}, score: {score + arr[curr_r][curr_c]}")
            # print_board(arr)
            return

        if count == 4:
            # print(f"count: {count}, curr:{curr_r, curr_c}, score: {score+arr[curr_r][curr_c]}")
            # print_board(arr)
            ans = max(ans, score + arr[curr_r][curr_c])
            return

        # countinue
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = curr_r+dr, curr_c+dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] > 0:
                curr_score = arr[nr][nc]
                if count == 2:
                    arr[nr][nc] = 0
                    dfs(arr, curr_r, curr_c, count+1, score+curr_score)
                    arr[nr][nc] = curr_score

                arr[nr][nc] = 0
                dfs(arr, nr, nc, count+1, score+curr_score)
                arr[nr][nc] = curr_score

    for r in range(N):
        for c in range(M):
            first_score = score_board[r][c]
            score_board[r][c] = 0
            dfs(score_board, r, c, 1, first_score)
            score_board[r][c] = first_score


# ===output===
ans = 0
sol()
print(ans)
