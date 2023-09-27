# (0.4, lv3) dfs__Softeer_7_순서대로방문하기

# answer: 차량이 이동 가능한 시나리오의 수

# N*N grid [0, 1(WALL)]
# M개 지점을 순서대로 방문
# 방문한 지점은 다시 방문 X


import sys
from typing import List

# === input ===
N, M = map(int, input().split())
GRID = [list(map(int, input().split())) for _ in range(N)]
POINT_LIST = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

WALL, POINT = 1, 2
answer = 0


# === algorithm ===
def init():
    global GRID
    for point_r, point_c in POINT_LIST:
        GRID[point_r][point_c] = POINT


def dfs(r, c, point_idx: int, visited: List[List[bool]]):
    global answer

    # 마지막 도착점을 지난 경우
    if point_idx == M:
        answer += 1
        return

    # 마지막 도착점 이전인 경우

    # TODO: 방문해야 하는 지점 -> point_idx + 1
    # TODO: deepcopy visited

    for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and GRID[nr][nc] != WALL and not visited[nr][nc]:
            next_visited = [visited[r][:] for r in range(N)]
            next_visited[nr][nc] = True
            if GRID[nr][nc] == POINT:  # 방문해야 하는 지점인 경우
                if [nr, nc] == POINT_LIST[point_idx]:  # 순서에 맞게 방문한 경우
                    dfs(nr, nc, point_idx + 1, next_visited)
                else:  # 순서가 맞지 않는 경우
                    continue
            else:
                dfs(nr, nc, point_idx, next_visited)


def solution():
    init()
    dfs(*POINT_LIST[0], 1, [[False] * N for _ in range(N)])


# === output ===
solution()
print(answer)
