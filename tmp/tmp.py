# (0.5, 골3) BOJ_23288_주사위굴리기2

# 22:45~ 23:15

# N*M grid [1,1 ~]

# 이동
# 1. 이동 방향으로 1칸. 이동 방향에 칸이 없다면, 방향을 반대로 바꾸어 한 칸
# 2. 도착한 칸(B)에 대한 점수 (주사위 아랫면 (A)
    # 1) A > B -> 이동 방향 시계 방향으로 회전
    # 2) A < B -> counter clockwise
    # 3) A == b -> 변화 x


# === input ===
N, M, K = map(int, input().split())
GRID = [list(map(int, input().split())) for _ in range(N)]
DIRECTION_LIST = [[0, 1], [1, 0], [0, -1], [-1, 0]]     # 시계 방향
# memo_grid = [[[0]*4 for _ in range(M)] for _ in range(N)]
memo_grid = [[0]*M for _ in range(N)]


# === algorithm ===
class Dice:

    # 동 남 서 북
    __roll_list = [[4, 2, 1, 6, 5, 3],
                   [2, 6, 3, 4, 1, 5],
                   [3, 2, 6, 1, 5, 4],
                   [5, 1, 3, 4, 6, 2]]

    def __init__(self, dice=None):
        if dice:
            self.dice = dice.dice
            self.r, self.c = dice.r, dice.c
            self.direction_id = dice.direction_id
        else:
            self.dice = list(range(1, 7))
            self.r, self.c = 0, 0
            self.direction_id = 0

    def __roll_dice(self):
        self.dice = [self.dice[Dice.__roll_list[self.direction_id][i] - 1] for i in range(6)]

    def __str__(self):
        return f"위치: {self.r, self.c, self.direction_id}, dice: {self.dice}"

    def get_bottom(self):
        return self.dice[5]

    # 이동 이후 방향 id 얻기
    def __get_next_direction_id(self) -> int:
        r, c, d = self.r, self.c, self.direction_id
        bottom_num = self.get_bottom()

        if bottom_num > GRID[r][c]:
            return (d + 1) % 4
        elif bottom_num < GRID[r][c]:
            return (d - 1) % 4
        else:
            return d

    def move_dice(self):
        r, c, d = self.r, self.c, self.direction_id

        dr, dc = DIRECTION_LIST[d]
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M:
            self.r, self.c = nr, nc
            self.__roll_dice()
            self.direction_id = self.__get_next_direction_id()
        else:
            self.direction_id = (d + 2) % 4
            self.move_dice()


def get_score(dice: Dice) -> int:
    global memo_grid
    #
    # if memo_grid[dice.r][dice.c][dice.direction_id] != 0:
    #     return memo_grid[dice.r][dice.c][dice.direction_id]
    #
    # dice_copy = Dice(dice)
    #
    # score = 1
    # grid_num = GRID[dice.r][dice.c]
    # while True:
    #     print("before:", dice_copy)
    #     dice_copy.move_dice()
    #     # 이동했는데 숫자가 다르면 break
    #     if GRID[dice_copy.r][dice_copy.c] != grid_num:
    #         break
    #     score += 1
    #     print("after:", dice_copy)
    #
    # del dice_copy
    # score *= grid_num
    # memo_grid[dice.r][dice.c][dice.direction_id] = score
    # return score

    if memo_grid[dice.r][dice.c] != 0:
        return memo_grid[dice.r][dice.c]


    def bfs():
        queue=


    score  = bfs() * GRID[dice.r][dice.c]
    memo_grid[dice.r][dice.c] = score
    return score


def solution():
    answer = 0

    dice = Dice()
    for _ in range(K):
        dice.move_dice()
        answer = get_score(dice)

    return answer


# === output ===
print(solution())
