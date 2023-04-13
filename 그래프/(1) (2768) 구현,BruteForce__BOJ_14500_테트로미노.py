# (1) 구현__BOJ_14500_테트로미노

# 점수판이 주어짐.
# 점수판에 테트로미노를 적절히 놓아서 수들의 합이 최대가 되도록
# 회전, 대칭 가능

# ===input===
N, M = map(int, input().split())
score_board = [list(map(int, input().split())) for _ in range(N)]


# ===algorithm===
tetromino_list = [[(0, 0), (0, 1), (0, 2), (0, 3)],     # ㅡ
                  [(0, 0), (1, 0), (2, 0), (3, 0)],     # ㅣ
                  [(0, 0), (0, 1), (1, 0), (1, 1)],     # ㅁ
                  [(0, 0), (1, 0), (2, 0), (2, 1)],     # ㄴ
                  [(0, 0), (1, 0), (2, 0), (2, -1)],
                  [(0, 0), (1, 0), (2, 0), (0, 1)],
                  [(0, 0), (1, 0), (2, 0), (0, -1)],
                  [(0, 0), (0, 1), (0, 2), (1, 0)],
                  [(0, 0), (0, 1), (0, 2), (1, 2)],
                  [(0, 0), (0, 1), (0, 2), (-1, 0)],
                  [(0, 0), (0, 1), (0, 2), (-1, 2)],
                  [(0, 0), (1, 0), (1, 1), (2, 1)],      # ㄹ
                  [(0, 0), (1, 0), (1, -1), (2, -1)],
                  [(0, 0), (0, 1), (1, 1), (1, 2)],
                  [(0, 0), (0, 1), (1, 0), (1, -1)],
                  [(0, 0), (0, 1), (0, 2), (1, 1)],      # ㅜ
                  [(0, 0), (0, 1), (0, 2), (-1, 1)],
                  [(0, 0), (1, 0), (2, 0), (1, 1)],
                  [(0, 0), (1, 0), (2, 0), (1, -1)]]



def do_tetromino(tetromino: list):

    max_score = 0

    for board_r in range(N):
        for board_c in range(M):
            score = 0
            for dr, dc in tetromino:
                tet_r, tet_c = board_r+dr, board_c+dc
                if 0 <= tet_r < N and 0 <= tet_c < M:
                    score += score_board[tet_r][tet_c]
                else:
                    score = 0
                    break
            max_score = max(max_score, score)
    return max_score


# ===output===
ans = 0
for tet in tetromino_list:
    ans = max(ans, do_tetromino(tet))
print(ans)