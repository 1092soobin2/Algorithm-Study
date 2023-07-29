# (골3, 0.5) Codetree_바이러스실험


# N*N
# 초기: 5 nutriment, M virus



from typing import List
import heapq

# === input ===
DEBUG = False
N, M, K = map(int, input().split())
# M virus ( r, c, age-1)

class Virus:
    def __init__(self, age):
        self.age = age
        self.dead = False

    def __str__(self):
        return f"{self.age}"

    def __lt__(self, other):
        return self.age < other.age


# board
class Board:
    nutrient: List[List[int]] = [[5] * N for _ in range(N)]
    ADDITION: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]
    # min age 순 힙큐
    virus: List[List[List]] = [[list() for _ in range(N)] for _ in range(N)]

    def __init__(self):
        for _ in range(M):
            r, c, age = map(int, input().split())
            heapq.heappush(Board.virus[r-1][c-1], Virus(age))

    # 1. nourish
    @classmethod
    def __nourish(cls):
        # virus가 속한 칸의 nutriment 섭취
        # virus가 여럿인 경우, 어린 virus부터
        for r in range(N):
            for c in range(N):
                if not Board.virus[r][c]:
                    continue
                virus_list = []
                while Board.virus[r][c]:
                    virus = heapq.heappop(Board.virus[r][c])
                    # 본인 나이만큼 섭취하지 못한 virus -> dead: nutriment += age // 2
                    if Board.nutrient[r][c] < virus.age:
                        virus.dead = True
                        Board.nutrient[r][c] += virus.age // 2
                    # 나이만큼의 양분을 섭취한 virus -> age += 1
                    else:
                        Board.nutrient[r][c] -= virus.age
                        virus.age += 1
                        heapq.heappush(virus_list, virus)
                Board.virus[r][c] = virus_list
        Board.print_nutrient("after nourishing")
        Board.print_virus("after nourishing")

    # 2. propagate
    @classmethod
    def __propagate(cls):
        # virus.age % 5 == 0 -> 인접 8 칸에 Virus(age=1)
        for r in range(N):
            for c in range(N):
                for virus in Board.virus[r][c]:
                    if virus.age % 5 == 0:
                        for dr, dc in [[-1, -1], [0, -1], [1, -1], [1, 0],
                                       [1, 1], [0, 1], [-1, 1], [-1, 0]]:
                            nr, nc = r + dr, c + dc
                            # 범위 벗어난 곳에는 번식 X
                            if 0 <= nr < N and 0 <= nc < N:
                                heapq.heappush(Board.virus[nr][nc], Virus(1))
        Board.print_virus("after propagation")

    # 3. add_nutrient
    @classmethod
    def __add_nutrient(cls):
        for r in range(N):
            for c in range(N):
                Board.nutrient[r][c] += Board.ADDITION[r][c]
        Board.print_nutrient("after addition")


    @classmethod
    def one_cycle(cls):
        cls.__nourish()
        cls.__propagate()
        cls.__add_nutrient()

    @classmethod
    def get_number_of_virus(cls) -> int:
        ret_int = 0
        for r in range(N):
            for c in range(N):
                ret_int += len(Board.virus[r][c])

        return ret_int

    @classmethod
    def print_nutrient(cls, title=""):
        if not DEBUG:
            return
        print("================================")
        print("[nutrient]" + title)
        for r in range(N):
            for c in range(N):
                print(f"{Board.nutrient[r][c]:4}", end="")
            print()
        print("================================")

    @classmethod
    def print_virus(cls, title=""):
        if not DEBUG:
            return
        print("================================")
        print("[virus]" + title)
        for r in range(N):
            for c in range(N):
                print("[", end="")
                for v in Board.virus[r][c]:
                    print(v, end=" ")
                print("]", end="")
            print()
        print("================================")

# === algorithm ===
board = Board()
for _ in range(K):
    board.one_cycle()

# === output ===
# ans: k cycle 이후 살아있는 바이러스의 양
print(board.get_number_of_virus())
