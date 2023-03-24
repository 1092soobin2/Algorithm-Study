# BOJ_16236_아기상어_BFS
'''
NxN 크기의 공간 (N <= 20)
M마리 물고리
1마리 상어

물고기, 상어는 크기를 가지고 있다.
[상어]
-처음에 크기 2
-1초에 인접 한 칸 이동

-자신보다 큰 물고기가 있는 칸은 지나갈 수 X
-자신보다 작은 물고기는 먹을 수 있다.
-자신과 같은 물고기는 먹을 수 X, 지나갈 수 O

-먹 물고기 X -> 엄마 상어에게 도움 요청
-먹 물고기 O -> 가장 가까운 물고기 먹으러.
    -거리: 칸의 개수의 최솟값 (BFS)
    -가까운 물고기가 많으면 좌상단 물고기 먼저

- 이동과 동시에 물고기 먹으면 그 칸은 빈 칸이 된다.
- 물고기 수에 따라 크기 증가 (크기 증가 시마다 먹은 물고기 수 reset)
'''

from collections import deque

# ===input===
N = int(input())
SPACES = [list(map(int, input().split())) for _ in range(N)]


# ===algorithm===
# 1. 상어 클래스
class Shark:
    def __init__(self, row, col):
        self.height = 2
        self.num_of_eating_fishes = 0
        self.time = 0
        self.r, self.c = row, col

    def bfs(self) -> int :
        # 기본 2개 자료구조
        # visited = [[False] * N for _ in range(N)]
        visited_time = [[-1] * N for _ in range(N)]
        stack = deque([(self.r, self.c)])

        visited_time[self.r][self.c] = 0
        fish_flag = 1e9
        fish_loc_list = []

        # stack 이용
        while stack:
            r, c = stack.popleft()
            curr_time = visited_time[r][c]
            if curr_time == fish_flag:
                # Go and eat.
                fish_loc_list.sort(key=lambda x: (x[0], x[1]))
                # print(f"후보 물고기 위치 {fish_loc_list}")
                self.__eat_fish(fish_loc_list[0][0], fish_loc_list[0][1], fish_flag)
                return self.bfs()
            # print(f"{curr_time}:({r},{c}) ", end="->")

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N:
                    if SPACES[nr][nc] <= self.height and visited_time[nr][nc] == -1:
                        stack.append((nr, nc))
                        visited_time[nr][nc] = curr_time + 1
                        if 0 < SPACES[nr][nc] < self.height:
                            fish_flag = curr_time + 1
                            fish_loc_list.append((nr, nc))

        return self.time

    def __eat_fish(self, r, c, time):
        # print(f"\n이전 \t {self.r}, {self.c} \t{self.time} ")
        self.r, self.c = r, c                           # Go to the location
        self.time += time                               # Update time

        SPACES[r][c] = 0                                # Eat fish
        self.num_of_eating_fishes += 1
        if self.num_of_eating_fishes == self.height:    # Update height
            self.height += 1
            self.num_of_eating_fishes = 0

        # print(f"현재 \t {self.r}, {self.c} \t{self.time}, height:{self.height}")
        # for _ in range(N):
        #     print(SPACES[_])
        # print()

# 2. 상어 위치
row, col = 0, 0
for r in range(N):
    for c in range(N):
        if SPACES[r][c] == 9:
            row, col = r, c
            SPACES[r][c] = 0
            break

# 3. 탐색 시작
shark = Shark(row, col)
ans = shark.bfs()

# ===output===
print(ans)