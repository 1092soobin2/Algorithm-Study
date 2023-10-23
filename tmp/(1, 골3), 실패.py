# 21:50~

# 뱀 [길이(초기 1), 위치(초기 0, 0), 방향(우)]
# 사과 먹으면 길이가 늘어난다

# 이동
# 1. 길이를 늘려 머리를 다음 칸에 위치시킨다.
# 2. 벽이나, 자기 자신의 몸과 부딧히면 게임이 끝난다.
# 3. 이동 칸에 사과 O -> 사과 없어지고, 꼬리는 움직이지 않는다.
# 4. 이동 칸에 사과 X -> 꼬리가 한 칸 움직인다. 몸 길이는 변하지 않는다.

# answer: 게임이 몇 초에 끝나는지

# N * N board
from collections import deque


DIRECTION_LIST = [[-1, 0], [0, -1], [1, 0], [0, 1]]


class Snake:
    body = deque([[0, 0]])
    direction_id = 3
    direction_change_dict = dict()

    @classmethod
    def _get_next(cls, loc):
        dr, dc = DIRECTION_LIST[cls.direction_id]
        return [loc[0] + dr, loc[1] + dc]

    @classmethod
    def move(cls):
        global board

        cls.body.appendleft(cls._get_next(cls.body[0]))
        hr, hc = cls.body[0]
        print(f"di: {DIRECTION_LIST[cls.direction_id]}")
        if 0 <= hr < N and 0 <= hc < N and board[hr][hc] != SNAKE:
            if board[hr][hc] == APPLE:
                board[hr][hc] = SNAKE
            else:
                board[hr][hc] = SNAKE
                tr, tc = cls.body[-1]
                board[tr][tc] = 0
                cls.body.pop()
            return True
        else:
            return False

    @classmethod
    def check_direction(cls, time):
        if time in cls.direction_change_dict:
            change = cls.direction_change_dict[time]
            cls.direction_id = (cls.direction_id - 1) % 4 if change == "D" else (cls.direction_id + 1) % 4


# === input ===
N = int(input())
K = int(input())        # 사과의 개수
APPLE_LIST = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
D_CHANGE_LIST = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(L)]
board = [[0] * N for _ in range(N)]
APPLE, SNAKE = 1, 2


# === algorithm ===
def init():
    global board

    for r, c in APPLE_LIST:
        board[r][c] = APPLE
    board[0][0] = SNAKE

    Snake.direction_change_dict = dict(D_CHANGE_LIST)


def solution():
    init()

    time = 0
    while Snake.move():
        print(time)
        time += 1
        Snake.check_direction(time)

        for r in range(N):
            print(board[r])
        print()

    return time


# === output ===
print(solution())
