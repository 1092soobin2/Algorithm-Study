# (1) 수학,구현__BOJ_17143_낚시왕

# 1칸 1마리
# 상어 [위치[r, c], 속도s, 방향d, 크기 z]

# DIRECTION_LIST = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
DIRECTION_LIST = [(-1, 0), (0, -1), (1, 0), (0, 1)]


class Shark:
    def __init__(self, loc=None, speed=None, direction_id=None, size=None):
        self.loc = loc
        self.speed = speed
        self.direction_id = direction_id
        self.size = size
        self.dead = False

    def get_loc(self):
        return self.loc


#===input===
R, C, M = map(int, input().split())


#===algorithm===
def get_input():
    global shark_list, board

    def map_direction(d):
        if d == 1:
            return 0
        elif d == 2:
            return 2
        elif d == 3:
            return 3
        elif d == 4:
            return 1
        else:
            print("wrong direction")
            exit()

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        r, c = r-1, c-1
        d = map_direction(d)
        dr, dc = DIRECTION_LIST[d]
        if dr != 0:
            s = s % (2 * (R - 1))
        elif dc != 0:
            s = s % (2 * (C - 1))
        new_shark = Shark([r, c], s, d, z)
        shark_list.append(new_shark)
        board[r][c].add(new_shark)


def catch_shark(c) -> Shark:
    global board, shark_list

    shark = None
    for r in range(R):
        if board[r][c]:
            if len(board[r][c]) != 1:
                print("길이가 1이 아님")
                exit()
            shark = list(board[r][c])[0]
            board[r][c] = set()
            break
    if shark:
        # shark_list.remove(shark)
        shark.dead = True

    return shark


def move_sharks():
    global board, shark_list

    def move_one_shark(shark: Shark):
        prev_r, prev_c = shark.loc
        next_r, next_c = shark.loc
        # for _ in range(shark.speed):
        #     cand_r, cand_c = next_r+dr, next_c+dc
        #     if 0 <= cand_r < R and 0 <= cand_c < C:
        #         next_r, next_c = cand_r, cand_c
        #     else:
        #         shark.direction_id = (shark.direction_id + 2) % 4
        #         dr, dc = DIRECTION_LIST[shark.direction_id]
        #         next_r, next_c = next_r+dr, next_c+dc
        move = shark.speed
        while move > 0:
            if shark.direction_id == 0:
                if move > next_r:
                    move -= next_r
                    next_r = 0
                    shark.direction_id = (shark.direction_id + 2) % 4
                else:
                    next_r -= move
                    move = 0
            elif shark.direction_id == 2:
                if move > ((R - 1) - next_r):
                    move -= (R - 1) - next_r
                    next_r = R - 1
                    shark.direction_id = (shark.direction_id + 2) % 4
                else:
                    next_r += move
                    move = 0
            elif shark.direction_id == 1:
                if move > next_c:
                    move -= next_c
                    next_c = 0
                    shark.direction_id = (shark.direction_id + 2) % 4
                else:
                    next_c -= move
                    move = 0
            elif shark.direction_id == 3:
                if move > ((C - 1) - next_c):
                    move -= (C - 1) - next_c
                    next_c = C - 1
                    shark.direction_id = (shark.direction_id + 2) % 4
                else:
                    next_c += move
                    move = 0

        # arr 업데이트
        board[prev_r][prev_c].remove(shark)
        board[next_r][next_c].add(shark)
        # shark 업데이트
        shark.loc = [next_r, next_c]

    for s in shark_list:
        if s.dead:
            continue
        move_one_shark(s)


def update_board():
    global shark_list, board

    for r in range(R):
        for c in range(C):
            if len(board[r][c]) > 1:
                # Find a biggest shark.
                biggest_shark = Shark(size=-1)
                for shark in board[r][c]:
                    if shark.size > biggest_shark.size:
                        biggest_shark = shark
                # shark list 업데이트
                # shark_list = list(set(shark_list) - set(board[r][c]))
                # shark_list.append(biggest_shark)
                for s in board[r][c]:
                    if s == biggest_shark:
                        continue
                    s.dead = True
                # arr 업데이트
                board[r][c] = {biggest_shark}


# ===output===
shark_list = []
board = [[set() for _ in range(C)] for _ in range(R)]
get_input()

answer = 0
for person_c in range(C):
    caught_shark = catch_shark(person_c)
    if caught_shark:
        answer += caught_shark.size
    move_sharks()
    update_board()

print(answer)
