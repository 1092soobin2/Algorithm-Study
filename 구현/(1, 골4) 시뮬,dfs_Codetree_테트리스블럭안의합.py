# (1, 골4) 시뮬,dfs_Codetree_테트리스블럭안의합 20~


# N*M grid

from typing import List

# === input ===
N, M = map(int, input().split())
GRID = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
def solution():
    max_sum = [0]
    visited_grid = [[False] * M for _ in range(N)]

    def dfs(curr_r, curr_c, num_of_block, sum_of_block):
        # print(f"in dfs: {curr_r, curr_c}, num: {num_of_block}, sum: {sum_of_block}")
        if num_of_block == 4:
            max_sum[0] = max(max_sum[0], sum_of_block)
            visited_grid[curr_r][curr_c] = False
            return

        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            next_r, next_c = curr_r + dr, curr_c + dc
            if 0 <= next_r < N and 0 <= next_c < M and not visited_grid[next_r][next_c]:
                visited_grid[next_r][next_c] = True
                dfs(next_r, next_c, num_of_block + 1, sum_of_block + GRID[next_r][next_c])

                if num_of_block == 2:
                    visited_grid[next_r][next_c] = True
                    dfs(curr_r, curr_c, num_of_block + 1, sum_of_block + GRID[next_r][next_c])

        visited_grid[curr_r][curr_c] = False

    for r in range(N):
        for c in range(M):
            # print("\n\n\n=======================================")
            # print(f"start{r,c}")
            visited_grid = [[False] * M for _ in range(N)]
            visited_grid[r][c] = True
            dfs(r, c, 1, GRID[r][c])

    return max_sum[0]


# === output ===
print(solution())
