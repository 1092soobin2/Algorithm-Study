# (0.5, 골4) BOJ_3190_뱀

# 19:19~

# Dummy라는 도스게임이 있다.

# 뱀 [위치(0, 0), 길이(1), 방향(오른쪽)]
# 사과를 먹으면 길이가 늘어남.
# 벽 || 자기자신과 부딪히면 게임이 끝난다.

# N*N board [사과]
# 1. 머리를 다음 칸에 위치
# 2. 벽 || 자기자신과 부딪히면 게임 종료
# 3. 이동 칸에 사과 O -> 사과 없어지고, 꼬리 움직 X
# 4. 이동 칸에 사과 X -> 꼬리 움직 O

# answer: 게임이 몇 초에 끝나는지

from collections import deque


# ===  ===
# L -> left / D -> right
N = int(input())
K = int(input())
APPLE_LIST = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
SNAKE_CHANGE_LIST = [list(input().split()) for _ in range(L)]


# === algorithm ===
class Snake:

    body = deque()
    DIRECTION_LIST = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    direction_id = 3

    @classmethod
    def turn(cls, info):
        if info == 'L':
            cls.direction_id = (cls.direction_id + 1) % 4
        else:
            cls.direction_id = (cls.direction_id - 1) % 4

    @classmethod
    def increase(cls):
        dr, dc = Snake.DIRECTION_LIST[cls.direction_id]
        cls.body.appendleft([cls.body[0][0] + dr, cls.body[0][1] + dc])
        return cls.body[0]

    @classmethod
    def decrease(cls):
        return cls.body.pop()


class Board:

    grid = [[0]*N for _ in range(N)]
    EMPTY, APPLE, SNAKE = 0, 1, 2
    snake_change = 0

    @classmethod
    def init(cls):

        for r, c in APPLE_LIST:
            cls.grid[r-1][c-1] = cls.APPLE

        Snake.body.append([0, 0])
        cls.grid[0][0] = cls.SNAKE

    @classmethod
    def move_snake(cls, time):

        # 1. 머리를 다음 칸에 위치
        nr, nc = Snake.increase()

        # 2. 벽 || 자기자신과 부딪히면 게임 종료
        if not (0 <= nr < N and 0 <= nc < N and cls.grid[nr][nc] != cls.SNAKE):
            return False

        # 3. 이동 칸에 사과 O -> 사과 없어지고, 꼬리 움직 X
        if cls.grid[nr][nc] == cls.APPLE:
            cls.grid[nr][nc] = cls.SNAKE
        # 4. 이동 칸에 사과 X -> 꼬리 움직 O
        else:
            cls.grid[nr][nc] = cls.SNAKE
            tail_r, tail_c = Snake.decrease()
            cls.grid[tail_r][tail_c] = cls.EMPTY

        # 방향 정보 체크
        if cls.snake_change < len(SNAKE_CHANGE_LIST) and int(SNAKE_CHANGE_LIST[cls.snake_change][0]) == time:
            Snake.turn(SNAKE_CHANGE_LIST[cls.snake_change][1])
            cls.snake_change += 1

        return True

    @classmethod
    def print(cls):
        print("=================================")
        for r in range(N):
            for c in range(N):
                if cls.grid[r][c] == cls.SNAKE:
                    print(" ^", end="")
                elif cls.grid[r][c] == cls.EMPTY:
                    print(" _", end="")
                else:
                    print(" 0", end="")
            print()
        print("=================================")


def solution():
    Board.init()
    time = 1
    while Board.move_snake(time):
        time += 1

    return time


# === output ===
print(solution())
