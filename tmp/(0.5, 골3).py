# (0.5, 골3)


# 20 M ~


# N*N grid [1-6]
# dice [loc (init [1, 1]), direction (init right)]
# 마주한 면의 합 7
# m번 굴려짐
# 움직일 때마다, 인접하며 같은 숫자 칸의 합만큼 점수를 얻게 됨 == (점수 * 칸 개수)

# (bottom) > (grid[r][c]) -> clockwise
#           <             -> counter_clockwise

# 벽에 부딪히면 반사

from collections import deque


class Dice:
    location = [0, 0]
    DIRECTION_LIST = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    direction_id = 3
    side = [1, 2, 3, 4, 5, 6]
    roll_rule = [[2, 6, 3, 4, 1, 5],
                 [3, 2, 6, 1, 5, 4],
                 [5, 1, 3, 4, 6, 2],
                 [4, 2, 1, 6, 5, 3]]

    @classmethod
    def get_bottom_side(cls):
        return cls.side[5]

    @classmethod
    def change_direction(cls, clockwise=True):
        if clockwise:
            cls.direction_id = (cls.direction_id - 1) % 4
        else:
            cls.direction_id = (cls.direction_id + 1) % 4

    @classmethod
    def roll(cls):
        cls.side = [cls.side[i-1] for i in cls.roll_rule[cls.direction_id]]


class Board:
    grid = []
    total_score = 0

    @classmethod
    def get_score(cls, start):

        criteria = cls.grid[start[0]][start[1]]

        def bfs():

            score = 0

            r, c = start
            queue = deque([[r, c]])
            visited = [[False]*N for _ in range(N)]
            visited[r][c] = True

            while queue:
                r, c = queue.popleft()
                score += 1

                for dr, dc in Dice.DIRECTION_LIST:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and cls.grid[nr][nc] == criteria:
                        visited[nr][nc] = True
                        queue.append([nr, nc])
            return score
        return bfs() * criteria

    @classmethod
    def roll_dice(cls):
        dr, dc = Dice.DIRECTION_LIST[Dice.direction_id]
        nr, nc = Dice.location
        nr, nc = nr + dr, nc + dc

        if not (0 <= nr < N and 0 <= nc < N):
            Dice.direction_id = (Dice.direction_id + 2) % 4
            dr, dc = Dice.DIRECTION_LIST[Dice.direction_id]
            nr, nc = nr + dr, nc + dc

        Dice.location = [nr, nc]
        Dice.roll()
        cls.total_score += cls.get_score([nr, nc])

        if Dice.get_bottom_side() > cls.grid[nr][nc]:
            Dice.change_direction(clockwise=True)
        elif Dice.get_bottom_side() < cls.grid[nr][nc]:
            Dice.change_direction(clockwise=False)


# ===  ===
N, M = map(int, input().split())
Board.grid = [list(map(int, input().split())) for _ in range(N)]


# ===  ===
def solution():
    for _ in range(M):
        Board.roll_dice()

    return Board.total_score


# ===  ===
print(solution())
