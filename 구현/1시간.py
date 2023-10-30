#1 시간

# (0.5, 골2) Codetree_루돌프의반란

# 1~P 번의 산타들

import heapq
from typing import List


# === input ===
N, NUM_TURN, NUM_SANTA, SCORE_R2S, SCORE_S2R = map(int, input().split())
INPUT_RUDOLF_LOC = list(map(lambda x: int(x) - 1, input().split()))
INPUT_SANTA_LOC_LIST = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(NUM_SANTA)]


# === algorithm ===
class Santa:

    def __init__(self, loc):
        self.available = True
        self.score = 0
        self.loc = loc


class Game:

    santa_board = []
    santa_list: List[Santa] = []
    rudolf_loc = []

    # 1. 게임판 구성
    @classmethod
    def init(cls):
        # N*N grid [1, 1](좌상단) ~
        cls.santa_board = [[0] * N for _ in range(N)]
        for i in range(NUM_SANTA):
            sr, sc = INPUT_SANTA_LOC_LIST[i]
            cls.santa_list.append(Santa([sr, sc]))
            cls.santa_board[sr][sc] = i
        cls.rudolf_loc = INPUT_RUDOLF_LOC

    @classmethod
    def __move_santa(cls, santa: Santa, direction, dist):

        # 밀려난 칸에 산타가 있는 경우 상호작용 발생
        dr, dc = [direction[0] * dist, direction[1] * dist]
        sr, sc = santa.loc
        nr, nc = sr + dr, sc + dc

        if 0 <= nr < N and 0 <= nc < N:
            santa.loc = [sr, sc]
            if cls.santa_board[sr][sc] != 0:
                cls.__interact_santa(santa, direction)
        else:
            # 이동 위치가 게임 판 밖이면 탈락함.
            santa.available = False
            cls.santa_board[sr][sc] = 0

    # 2. 루돌프의 움직임
    @classmethod
    def __move_rudolf(cls):
        [rr, rc] = cls.rudolf_loc

        # 1. 탈락하지 않은 산타 중, 가장 가까운 산타를 향해 1칸 돌진
        pq = []
        for santa in cls.santa_list:

            if not santa.available:
                continue
            [sr, sc] = santa.loc
            dist = (rr - sr) ** 2 + (rc - sc) ** 2
            heapq.heappush(pq, (dist, -sr, -sc, santa))        # 2명 이상이면, max(r), max(c)
            # TODO: 없으 면 게임 종료 ..? 여기서..?

        # 2. # 인접 8칸 중 하나, 가장 가까워지는 방향으로
        sr, sc = [-pq[0][1], -pq[0][2]]
        direction = [0, 0]
        if sr == rr:        # -   -
            direction = [0, 1 if rc < sc else -1]
        elif sc == rc:      # |
            direction = [1 if rr < sr else -1, 0]
        else:
            direction = [1 if rr < sr else -1, 1 if rc < sc else -1]

        # 루돌프 움직임
        cls.rudolf_loc = [rr + direction[0], rc + direction[1]]
        # 충돌
        if [sr, sc] == [rr, rc]:
            cls.__crash('r2s', pq[0][3], direction)

    # 4. 충돌
    @classmethod
    def __crash(cls, crashing: str, santa: Santa, direction: list):
        # 산타 & 루돌프가 같은 칸이면 충돌 발생
        # 루돌프 움직 충돌 -> 산타 +C, 산타가 C만큼, 루돌프 이동 방향으로 밀려남
        if crashing == 'r2s':
            santa.score += SCORE_R2S
            cls.__move_santa(santa, direction, SCORE_R2S)
        # 산타   움직 충돌 -> 산타 +D, 산타가 자신의 반대 방향으로 D만큼 밀려남
        elif crashing == 's2r':
            santa.score += SCORE_S2R
            cls.__move_santa(santa, [-direction[0], - direction[1]], SCORE_S2R)

# M 개의 턴
# 루돌프 움직임 -> 1~P 산타가 순서대로 움직임
# 기절 | 격자 밖 (탈락한) 빠져나간 산타들은 움직이지 못한다.
# 두 칸 사이의 거리 = (r1- r2) ** 2 + (c1 - c2) ** 2


    # 3. 산타의 움직임
    # 기절 | 탈락 산타는 움직 X
    # 다른 산타가 있는 칸 | 경계 밖 으로는 움직이지 못한다.
    # 움직일 수 있는 칸이 없으면 움직이지 않는다.
    # 움직일 수 있더라도 루돌프로부터 가까워질 수 있는 방법이 없다면 움직이지 않는다.
    # 인접 4칸 중 한 곳으로 이동 가능
    # 상우하좌 우선순위에 맞춰 움직인다.


    # 5. 상호작용
    @classmethod
    def __interact_santa(cls, new_santa, direction):
        pass
        # 해당 칸에 있던 산타는 / 이동해온 산타의 이동 방향
        # / 으로 1칸 밀려남
        # 그 옆에 산타가 있다면 연쇄적으로 상호작용 일어남
        # 게임판 밖으로 밀혀나면 탈락함

# 6. 기절
# 산타는 루돌프와의 충돌 후 기절
# 2턴 후에 정상 상태가 됨.
# 루돌프는 기절한 산타에게 돌진 가능

# 7. 게임 종료
# M번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 종료
# P명의 산타가 모두 종료되면 게임 종료
# 아직 탈락하지 않은 산타들에게는 1점씩 추가 부여
# === output ===
