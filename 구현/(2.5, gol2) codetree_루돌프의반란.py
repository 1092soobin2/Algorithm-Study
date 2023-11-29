# (1, gol2) codetree_루돌프의반란

# 1:15 + 13:17~
# 1-P santa


# 5. 상호작용
# 착지 칸에 산타 -> santa.move(1, 방향)

# 6. 기절
# 충돌 후 기절,


from typing import List
import heapq
from enum import Enum


class Santa:

    class Status(Enum):
        ALIVE, BLACKED_OUT, DEAD = 0, 1, 2

    grid: List[List[int]] = []
    EMPTY = -1

    DIRECTION_LIST = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, loc):
        self.status = Santa.Status.ALIVE
        self.score = 0
        self.loc = loc
        self.blacked_turn = 0

    def black_out(self):
        self.status = Santa.Status.BLACKED_OUT
        self.blacked_turn = 2

    def check_move(self) -> list:
        pq = []     # (거리, r, c)
        r, c = self.loc
        # 루돌프에게 가까워지는 방향으로 1칸 이동
        now_dist = get_dist(self.loc, rudolf.get_loc())
        # 인접 4칸, 여러 개라면 상->우->히->좌
        for direction_priority, [dr, dc] in enumerate(Santa.DIRECTION_LIST):
            nr, nc = r + dr, c + dc
            # 다른 산타 칸 || 경계 밖으로는 움직이지 않음
            if 0 <= nr < N and 0 <= nc < N and Santa.grid[nr][nc] == Santa.EMPTY:
                next_dist = get_dist([nr, nc], rudolf.get_loc())
                # 가깝 칸 X -> 방향 X
                if next_dist < now_dist:
                    heapq.heappush(pq, (next_dist, direction_priority))
        return Santa.DIRECTION_LIST[pq[0][1]] if pq else None

    def move(self, speed: int, direction: list):
        r, c = self.loc
        dr, dc = direction
        nr, nc = r + dr * speed, c + dc * speed
        if not (0 <= nr < N and 0 <= nc < N):
            self.status = Santa.Status.DEAD
            Santa.grid[r][c] = Santa.EMPTY
        else:
            if rudolf.get_loc() == [nr, nc]:
                Santa.grid[nr][nc] = Santa.grid[r][c]
                Santa.grid[r][c] = Santa.EMPTY
                self.loc = [nr, nc]
                bomb(self, True, [-dr, -dc])
            else:
                if Santa.grid[nr][nc] != Santa.EMPTY:
                    santa2 = santa_list[Santa.grid[nr][nc]]
                    santa2.move(1, direction)
                Santa.grid[nr][nc] = Santa.grid[r][c]
                Santa.grid[r][c] = Santa.EMPTY
                self.loc = [nr, nc]

    def one_turn(self):
        if self.status != Santa.Status.DEAD:
            self.score += 1
        if self.status == Santa.Status.BLACKED_OUT:
            self.blacked_turn -= 1
            if self.blacked_turn == 0:
                self.status = Santa.Status.ALIVE
        return self.status

    def get_loc(self):
        return self.loc

    def __str__(self):
        return f"상태: {self.status}, 위치:{self.loc}, 블랙 아웃: {self.blacked_turn}, 점수: {self.score}"\


    @classmethod
    def print_grid(cls):

        for r in range(N):
            for c in range(N):
                if [r, c] == rudolf.get_loc():
                    print(f"R", end="")
                elif Santa.grid[r][c] == Santa.EMPTY:
                    print("_", end="")
                else:
                    santa = santa_list[Santa.grid[r][c]]
                    if santa.status == Santa.Status.DEAD:
                        print("_", end="")
                    else:
                        print(f"{Santa.grid[r][c]:1}", end="")
            print()


class Rudolf:

    DIRECTION_LIST = [[-1, 0], [-1, -1], [0, -1], [1, -1],\
                      [1, 0], [1, 1], [0, 1], [-1, 1]]

    def __init__(self, loc):
        self.loc = loc

    def get_loc(self):
        return self.loc

    def move(self):
        # 2. 루돌프의 움직임
        def get_direction(santa_loc):
            sr, sc = santa_loc

            if sr == self.loc[0]:
                dr, dc = 0, (1 if sc > self.loc[1] else -1)
            elif sc == self.loc[1]:
                dr, dc = (1 if sr > self.loc[0] else -1), 0
            else:
                dr, dc = (1 if sr > self.loc[0] else -1), (1 if sc > self.loc[1] else -1)

            return [dr, dc]

        # 가장 가까운 산타로 1칸 돌진
        pq = []         # (거리, r, c)
        for santa in santa_list:
            # 게임에서 탈락하지 않은 산타 중,
            if santa.status != Santa.Status.DEAD:
                r, c = santa.get_loc()
                # 2명 이상 -> max(r), max(c)
                heapq.heappush(pq, (get_dist(santa.get_loc(), self.loc), -r, -c))

        # 인접 8칸
        r, c = self.loc
        dr, dc = get_direction([-pq[0][1], -pq[0][2]])
        r, c = r + dr, c + dc
        if Santa.grid[r][c] != Santa.EMPTY:
            bomb(santa_list[Santa.grid[r][c]], False, [dr, dc])
        self.loc = [r, c]

    def __str__(self):
        return f"위치: {self.loc}"


# ===
def get_dist(loc1, loc2):
    [r1, c1], [r2, c2] = loc1, loc2
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def bomb(santa, santa_to_rudolf: bool, santa_direction):
    # 4. 충돌
    # 루->산 산.score += C, santa.move(C, 루돌픕 방향)
    # 산->루 산.score += D, santa.move(D, 자신 반대 방향)

    number = D if santa_to_rudolf else C

    santa.score += number
    santa.black_out()
    print_debug("bomb")
    santa.move(number, santa_direction)


def move_all_santa():
    # 3. 산타의 움직임

    # 1-P 순서대로 움직임
    for santa in santa_list:
        # 기절|탈락 산타는 움직일 수 없음
        if santa.status == Santa.Status.ALIVE:
            next_direction = santa.check_move()
            # 움직 칸 X -> 움직 X
            if next_direction:
                santa.move(1, next_direction)


def elapse_one_santa():
    game_end = True

    for santa in santa_list:
        if santa.one_turn() != Santa.Status.DEAD:
            game_end = False

    return game_end


def print_debug(title=""):
    if not DEBUG:
        return

    print("=====" + title)
    Santa.print_grid()
    print('\n'.join(list(map(str, santa_list))))
    print("======")


def solution():
    # 1. 게임판
    # N*N grid [1,1]~
    # 유클리드 거리
    # M turn -> 루돌프 -> 산타

    print_debug()

    # rudolf.move()
    # print_debug("rudlof")
    #
    # game_end = move_all_santa()
    # for santa in santa_list:
    #     santa.one_turn()
    # print_debug("santa")

    for _ in range(M):
        rudolf.move()
        print_debug("rudolf")

        move_all_santa()
        if elapse_one_santa():
            break

        print_debug("santa")

    return [santa.score for santa in santa_list]


# ===
N, M, P, C, D = map(int, input().split())
rudolf = Rudolf(list(map(lambda x: int(x) -1, input().split())))
Santa.grid = [[Santa.EMPTY]*N for _ in range(N)]
santa_list: List[Santa] = [None]*P
for _ in range(P):
    santa_num, sr, sc = map(lambda x: int(x) -1, input().split())
    santa_list[santa_num] = Santa([sr, sc])
    Santa.grid[sr][sc] = santa_num


# ===
DEBUG = False
print(*solution())
