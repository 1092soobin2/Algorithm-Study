# (1, gol2) codetree_루돌프의반란

# 22:44~

# 1-P santa


# 1. 게임판
# N*N grid [1,1]~
# 유클리드 거리


# 5. 상호작용
# 착지 칸에 산타 -> santa.move(1, 방향)

# 6. 기절
# 충돌 후 기절,


from typing import List
import heapq


class Santa:

    ALIVE, BLACKED_OUT, DEAD = 0, 1, 2
    grid: List[List[int]] = []

    DIRECTION_LIST = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, loc):
        self.status = Santa.ALIVE
        self.score = 0
        self.loc = loc
        self.blacked_turn = 0

    def black_out(self):
        self.status = Santa.BLACKED_OUT
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
            if 0 <= nr < N and 0 <= nc < N and Santa.grid[nr][nc] == 0:
                next_dist = get_dist(self.loc, rudolf.get_loc())
                # 가깝 칸 X -> 방향 X
                if next_dist < now_dist:
                    heapq.heappush(pq, (next_dist, direction_priority))
        return Santa.DIRECTION_LIST[pq[0][1]] if pq else None

    def move(self, speed: int, direction: list):
        r, c = self.loc
        dr, dc = direction
        nr, nc = r + dr * speed, r + dc * speed
        if not (0 <= nr < N and 0 <= nc < N):
            self.status = Santa.DEAD
        else:
            if rudolf.get_loc() == self.loc:
                self.black_out()
                bomb(self, True, direction)
            elif Santa.grid[nr][nc] != 0:
                santa2 = santa_list[Santa.grid[nr][nc]]
                santa2.move(1, direction)
            Santa.grid[nr][nc] = Santa.grid[r][c]
            Santa.grid[r][c] = 0
            self.loc = [nr, nc]

    def one_turn(self):
        if self.status == Santa.BLACKED_OUT:
            self.blacked_turn += 1
            if self.blacked_turn == 2:
                self.status = Santa.ALIVE

    def get_loc(self):
        return self.loc


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
                dr, dc = self.loc[0], self.loc[1] + (1 if sc > self.loc[1] else -1)
            elif sc == self.loc[1]:
                dr, dc = self.loc[0] + (1 if sr > self.loc[0] else -1), sc
            else:
                dr, dc = self.loc[0] + (1 if sr > self.loc[0] else -1), self.loc[1] + (1 if sc > self.loc[1] else -1)

            return [dr, dc]

        # 가장 가까운 산타로 1칸 돌진
        pq = []         # (거리, r, c)
        for santa in santa_list:
            # 게임에서 탈락하지 않은 산타 중,
            if santa.status != Santa.DEAD:
                r, c = santa.get_loc()
                # 2명 이상 -> max(r), max(c)
                heapq.heappush(pq, (get_dist(santa.get_loc(), self.loc), -r, -c))

        # 인접 8칸
        r, c = self.loc
        dr, dc = get_direction([-pq[0][1], -pq[0][2]])
        r, c = r + dr, c + dc
        if Santa.grid[r][c] != 0:
            bomb(santa_list[Santa.grid[r][c]], False, [-dr, -dc])


# ===
N, M, P, C, D = map(int, input().split())
rudolf = Rudolf(list(map(int, input().split())))
Santa.grid = [[0]*N for _ in range(N)]
santa_list: List[Santa] = [None]*(N+1)
for _ in range(P):
    santa_num, sr, sc = map(int, input().split())
    santa_list[santa_num] = Santa([sr, sc])


# ===





def get_dist(loc1, loc2):
    [r1, c1], [r2, c2] = loc1, loc2
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def bomb(santa, santa_to_rudolf: bool, santa_direction):
    # 4. 충돌
    # 루->산 산.score += C, santa.move(C, 루돌픕 방향)
    # 산->루 산.score += D, santa.move(D, 자신 반대 방향

    number = D if santa_to_rudolf else C

    santa.soore += number
    santa.move(number, santa_direction)


def move_all_santa() -> bool:
    # 3. 산타의 움직임

    game_end = True

    # 1-P 순서대로 움직임
    for santa in santa_list:
        # 기절|탈락 산타는 움직일 수 없음
        if santa.status != DEAD:
            game_end = False
            if santa.status == Santa.ALIVE:
                next_direction = santa.check_move()
                # 움직 칸 X -> 움직 X
                if next_direction:
                    santa.move(1, next_direction)
    return game_end


def solution():
    dd


# ===

