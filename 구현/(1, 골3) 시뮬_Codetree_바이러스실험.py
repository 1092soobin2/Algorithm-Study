# (1, 골3) Codetree_바이러스실험  50 ,

# N*N grid [essence: 5]
# M viruses [age]

# 1 Cycle

# ans: alive virus after k cycle

# import heapq
from collections import deque

# === input ===
N, M, K = map(int, input().split())
ADDITION_BOARD = [list(map(int, input().split())) for _ in range(N)]
virus_board = [[deque() for _ in range(N)] for _ in range(N)]
essence_board = [[5]*N for _ in range(N)]


# === algorithm ===
# get input about viruses
def init():
    global virus_board

    for _ in range(M):
        r, c, age = map(int, input().split())
        # heapq.heappush(virus_board[r-1][c-1], age)
        virus_board[r-1][c-1].append(age)

    # for r in range(N):
    #     for c in range(N):
    #         virus_board[r][c] = deque(sorted(virus_board[r][c]))

    print_debug("after init")


# 1. eat_essence
def eat_essence():
    #     1. as their age
    #     2. If there are several virus, from younger virus
    #     3. Eat -> age += 1, cannot Eat -> die and become essence -> age // 2
    for r in range(N):
        for c in range(N):
            new_virus_list = deque()
            new_essence = 0
            for virus_age in virus_board[r][c]:
                if virus_age <= essence_board[r][c]:
                    essence_board[r][c] -= virus_age
                    new_virus_list.append(virus_age + 1)
                else:
                    new_essence += virus_age // 2
            virus_board[r][c] = new_virus_list
            essence_board[r][c] += new_essence
    print_debug(f"after eat_essence()")


# 2. propagate
def propagate():
    for r in range(N):
        for c in range(N):
            for virus_age in virus_board[r][c]:
                # 1) if age % 5 == 0
                if virus_age % 5 == 0:
                    # 2) adjacent 8 (except out of board), emerge virus(age 1)
                    for dr, dc in [[-1, -1], [0, -1], [1, -1], [1, 0],
                                   [1, 1], [0, 1], [-1, 1], [-1, 0]]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            virus_board[nr][nc].appendleft(1)
    print_debug(f"after propagate()")


# 3. add_essence
def add_essence():
    for r in range(N):
        for c in range(N):
            essence_board[r][c] += ADDITION_BOARD[r][c]
    print_debug(f"after add_essence()")


def one_cycle():
    eat_essence()
    propagate()
    add_essence()


def solution():
    ans = 0
    init()
    for _ in range(K):
        one_cycle()
    for r in range(N):
        for c in range(N):
            ans += len(virus_board[r][c])
    return ans


def print_debug(title=""):
    if not DEBUG:
        return

    print("=========================")
    print(title)
    print("essence\t\t\t\tvirus")
    for r in range(N):
        for c in range(N):
            print(f"{essence_board[r][c]:4}", end="")
        print("\t", end="")
        for c in range(N):
            print(list(virus_board[r][c]), end=" ")
        print()
    print("=========================")


# === output ===
DEBUG = False
# DEBUG = True
print(solution())
