# (0.5, 골3) BOJ_16235_나무재테크

# N*N grid [1,1 ~ N,N]  [나무 (>= 0), essence (initailly 5)]
# M tree                [age]


from collections import deque
from typing import List
import sys
input = sys.stdin.readline


class Room:
    def __init__(self):
        self.essence = 5
        self.tree_ordered = deque([])

    def __str__(self):
        return f"essence: {self.essence}, tree:{self.tree_ordered}"


# === input ===
N, M, K = map(int, input().split())
ADDITION = [list(map(int, input().split())) for _ in range(N)]
grid: List[List[Room]] = [[Room() for _ in range(N)] for _ in range(N)]
ADJ_LIST = [[-1, -1], [0, -1], [1, -1], [1, 0],
            [1, 1], [0, 1], [-1, 1], [-1, 0]]
for _ in range(M):
    x, y, z = map(int, input().split())
    grid[x - 1][y - 1].tree_ordered.append(z)


# === algorithm ===
# spring
# summer
def spring_and_summer() -> List[List[int]]:
    global grid

    tree_5_loc = []

    for r in range(N):
        for c in range(N):
            room = grid[r][c]
            new_tree_ordered = deque()
            for tree_age in list(room.tree_ordered):
                # 1. age 만큼 양분 -> age += 1
                if room.essence >= tree_age:
                    # 2. 여러 개의 나무 -> 어린 나무부터 TODO: heapq tree_pq
                    room.essence -= tree_age
                    room.tree_ordered.popleft()
                    new_tree_ordered.append(tree_age + 1)
                    if (tree_age + 1) % 5 == 0:
                        tree_5_loc.append([r, c])
                else:
                    break

            # 3. age 만큼 못 먹으면 -> dead TODO: dead = True
            for tree_age in room.tree_ordered:
                # 1. 죽은 나무 -> 양분으로 변한다. TODO: essence += age // 2
                room.essence += tree_age // 2

            room.tree_ordered = new_tree_ordered

    return tree_5_loc


# autumn
def autumn(tree_5_loc):
    global grid

    def propagate():
        for dr, dc in ADJ_LIST:
            ar, ac = r + dr, c + dc
            if 0 <= ar < N and 0 <= ac < N:
                grid[ar][ac].tree_ordered.appendleft(1)

    # 1. if age % 5 == 0: 번식 (인접 8칸에 나이 1인 나무가 생긴다)
    for r, c in tree_5_loc:
        propagate()


# winter
def winter():
    global grid
    # 1. S2D2가 돌아다니며 땅에 양분 추가
    # 2. A만큼 양분 추가
    for r in range(N):
        for c in range(N):
            grid[r][c].essence += ADDITION[r][c]


def all_season():
    spring_and_summer()
    autumn()
    winter()


def solution():
    for _ in range(K):
        tree_5_loc = spring_and_summer()
        autumn(tree_5_loc)
        winter()

    answer = 0
    for r in range(N):
        for c in range(N):
            answer += len(grid[r][c].tree_ordered)
    return answer


# === output ===
print(solution())
