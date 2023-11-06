# (1, 골2) Codetree_루돌프의반란
# 22:30~

# 1~P santa
# Rudolf 박치기

# (1) 게임판의 구성
# N*N grid [1, 1]~
# M turn (루돌프 움직임 -> 산타 번호순으로 움직임) *기절/탈락한 산타는 못 움직임
# 두 칸 사이의 거리 = (r1-r2) ** 2 + (c1-c2) ** 2


# (6) black_out(santa)
# 산타는 루돌프와 충돌 후 기절 한다.
# k번째 턴이었다면, (k + 1) 번쨰 턴까지 기절하게 되어
# k + 2 째부터 정상상태가 됨
# 기절한 산타는 움직일 수 없음
# 루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있음

# (7) 게임 종료
# P 산타가 모두 탈락하게 된다면 즉시 종료 됨.
# 아직 탈락하지 않은 산타.score += 1

from typing import List
import heapq


class Santa:

    board = []

    def __init__(self, r, c):
        self.score = 0
        self.r, self.c = [r, c]
        self.dead = False
        self.black_out = 0

    def get_dead(self):
        return self.dead

    def move_santa(self, direction, length=1):
        dr, dc = direction
        nr, nc = self.r + dr*length, self.c + dc*length

        if not (0 <= nr < N and 0 <= nc < N):
            self.dead = True
            Santa.board[self.r][self.c] = -1
            return

        if [nr, nc] == [rudolf.r, rudolf.c]:
            bomb(self, r2s=False, direction=direction)                          # this santa move
        else:
            if Santa.check_santa_from_board(nr, nc):
                interact(self, Santa.get_santa_from_board(nr, nc), direction)       # another santa move
            Santa.board[nr][nc] = Santa.board[self.r][self.c]
            Santa.board[self.r][self.c] = -1
            self.r, self.c = nr, nc

    def set_black_out(self, diff=0):
        if diff != 0:
            self.black_out -= diff
        else:
            self.black_out = 2

    def get_black_out(self):
        return self.black_out

    @classmethod
    def check_santa_from_board(cls, r, c) -> bool:
        return Santa.board[r][c] != -1

    @classmethod
    def get_santa_from_board(cls, r, c):
        return santa_list[Santa.board[r][c]]


class Rudolf:

    def __init__(self, loc):
        self.r, self.c = loc

    # (2) 루돌프의 움직임
    def move(self):
        pq = []

        # 탈락하지 않은 산타 중, 가장 가까운 산타를 향해 1칸 돌진
        for santa in santa_list:
            if santa.get_dead():
                continue
            # max(r), max(c)
            heapq.heappush(pq, ((self.r-santa.r)**2 + (self.c-santa.c)**2, -santa.r, -santa.c, santa))

        # 인접 8칸 중 하나로 돌진할 수 있음.
        # 우선순위가 높은 산타를 향해 가장 가까워지는 방향으로 1칸 돌진
        # TODO: 여기서 pq 비어있는지 체크해야하나?
        sr, sc = -pq[0][1], pq[0][2]

        if self.r == sr:
            dr, dc = 0, 1 if sc > self.c else -1
        elif self.c == sc:
            dr, dc = 1 if sr > self.r else -1, 0
        else:
            dr, dc = 1 if sr > self.r else -1, 1 if sc > self.c else -1

        self.r += dr
        self.c += dc

        if [self.r, self.c] == [sr, sc]:
            bomb(pq[0][3], r2s=True, direction=[dr, dc])
            pq[0][3].set_black_out()


# === input ===
N, M, P, R2S_SCORE, S2R_SCORE = map(int, input().split())


# === algorithm ===
# board = []
santa_list: List[Santa] = []
rudolf: Rudolf = None


def init():
    global rudolf, santa_list
    Santa.board = [[-1] * N for _ in range(N)]

    rudolf = Rudolf(list(map(lambda x: int(x) - 1, input().split())))
    santa_list = [None] * P
    for _ in range(P):
        num, r, c = map(lambda x: int(x) - 1, input().split())
        santa_list[num] = Santa(r, c)
        Santa.board[r][c] = num


# (3) move_santa
def move_all_santa():
    # 1~P 순으로 움직임
    for santa in santa_list:
        # 기절 || 탈락한 산타는 못 움직임
        if santa.get_dead():
            continue
        elif santa.get_black_out() != 0:
            santa.set_black_out(diff=-1)

        pq = []
        original_dist = (santa.r - rudolf.r) ** 2 + (santa.c - rudolf.c) ** 2
        direction_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
        for i, [dr, dc] in enumerate(direction_list):
            nr, nc = santa.r + dr, santa.c + dc
            # 못 움직이는 칸: 다른 산타가 있는 칸 | 게임 판 밖
            if not (0 <= nr < N and 0 <= nc < N) or Santa.check_santa_from_board(nr, nc):
                continue
            new_dist = (nr - rudolf.r) ** 2 + (nc - rudolf.c) ** 2
            if new_dist < original_dist:
                # 인접 4칸 중 하나로 움직임, 여러 개라면, 상 -> 우 -> 하 -> 좌
                heapq.heappush(pq, (new_dist, i))

        # 움직일 수 있는 칸 X -> 안 움직임
        # 움직일 수 있는 칸 O && 가까워지는 방법 X -> 안 움직임
        if pq:
            santa.move_santa(direction_list[pq[0][1]])


# (4) bomb(santa, rudolf, r2c)
def bomb(santa: Santa, r2s: bool, direction):
    # 산타 && 루돌프 같은 칸이면 충돌
    # 루돌프 움직 충돌 -> 산타.score += C, 산타는 루돌프 이동 방향으로 C칸 밀려남        TODO: santa [score
    if r2s:
        santa.score += R2S_SCORE
        santa.move_santa(direction, R2S_SCORE)
    # 산타  움직 충돌 -> 산타.score += D, 산타는 자신 이동 반대 방향으로 D칸 밀려남
    else:
        santa.score += S2R_SCORE
        santa.move_santa([direction[0] * -1, direction[1] * -1], S2R_SCORE)

    # 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락된다                              TODO: move_santa
    # 밀려난 칸에 다른 산타가 있는 경우 상호작용이 발생                                 TODO: interact


# (5) interact(santa, direction)
def interact(santa1: Santa, santa2: Santa, direction):
    # 착지 칸에 다른 산타가 있다면, 산타는 해당 방향으로 1칸 밀려남
    santa2.move_santa(direction, 1)


def one_turn():
    rudolf.move()
    move_all_santa()

    alive = 0
    for santa in santa_list:
        if santa.get_dead():
            continue
        alive += 1
        santa.score += 1

    return True if alive != 0 else False


def solution():
    init()

    for _ in range(M):
        if not one_turn():
            break
        print([santa.score for santa in santa_list])

    answer = " ".join([str(santa.score) for santa in santa_list])
    return answer


# === output ===
print(solution())
