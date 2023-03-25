# __BOJ_23290_마법사상어와복제
'''
4x4 크기의 격자
(1,1) - (4,4)

M: 물고기 마릿수
S: 연습 횟수
ans: 연습 마친 후 격자에 있는 물고기의 수

이동방향: 8가지 (상하좌우, 대각선)
-둘 이상의 물고기가 같은 칸에 있을 수 있다.
-상어와 물고기가 같은 칸에 있을 수 있다.

상어의 마법 연습
1. 모든 물고기에게 복제 마법. 5번에서 복제된다.
2. 모든 물고기: 1칸 이동
    -상어가 있는 칸/물고기의 냄새가 있는 칸/격자 밖으로는 이동 할 수 없다.
    -각 물고기는 자신의 이동 방향을 45도 반시계 회전시킬 수 있다.
    -이동할 수 있는 칸 X -> 이동하지 않는다.
    -이동할 수 있는 칸 O -> 그 칸으로 이동
3. 상어: 연속 3칸 이동
    -상하좌우로 이동 가능
    -물고기가 있는 칸 -> 그 칸의 물고기는 격자에서 제외된다. 제외되면서 물고기의 냄새를 남긴다.
    -제외되는 물고기가 가장 많은 방법으로 이동한다.
    -방법이 여러 가지인 경우 사전 순으로 가장 앞서는 방법 (하단 노트)
4. 물고기의 냄새는 2회가 지나면 사라진다.
5. 1에서 사용한 복제마법이 와뇨된다. 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
'''

from collections import deque

# ===input===
M, S = map(int, input().slice())
MAP_EDGE = 4


class Fish:
    DIRECTION_TUP = ((1, -1), \
                     (0, -1), (-1, -1), (-1, 0), (-1, 1), \
                     (0, 1), (1, 1), (1, 0), (1, -1))

    def __init__(self, row, col, d):
        self.row = row
        self.col = col
        self.direction = d

    def move(self, r, c, d):
        self.row = r
        self.col = c
        self.direction = d


# class Space:
#     def __init__(self):
#         self.scent_bit = 0b00        # 죽으면 |0b01, 턴 바뀌면 <<1
#
#     def turn(self):
#         self.scent_bit <<= 1
#
#     def die(self):
#         self.scent_bit ||


# 물고기들 입력
space = [[[0b00]] * (MAP_EDGE+1) for _ in range(MAP_EDGE+1)]
fishes_list = []
for _ in range(M):
    fx, fy, d = map(int, input().slice())
    fishes_list.append(Fish(fx, fy, d))

# 상어 입력
sr, sc = map(int, input().slice())

# ===algorithm===

def move_shark(start : tuple):
    # 3칸 이동 dfs
    # 2개
    visited = [[-1] * (MAP_EDGE+1) for _ in range(MAP_EDGE+1)]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        r, c = queue.pop()

for _ in range(S):
    # 1. 물고기 복제
    dup_fishes = fishes_list

    # 2. 물고기 이동
    for fish in fishes_list:
        for i in range(8) :
            d = (fish.direction + i) % 8
            dr, dc = Fish.DIRECTION_TUP[d]
            nr, nc = fish.row + dr, fish.col + nc
            if 1 <= nr <= MAP_EDGE and 1 <= nc <= MAP_EDGE:
                if not(nr == sr and nc == sc) and space[nr][nc] == 0b00:
                    fish.move(nr, nc, d)

    # 3. 상어 이동



# ===output===