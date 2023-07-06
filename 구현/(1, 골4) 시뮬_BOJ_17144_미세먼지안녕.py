# (1, 골4) 시뮬_BOJ_17144_미세먼지안녕

# === input ===
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
CLEANER_LOC = []


# === algorithm ===
def init():
    global CLEANER_LOC

    for r in range(R):
        if room[r][0] == -1:
            CLEANER_LOC = [[r, 0], [r + 1, 0]]
            break

    print_debug(f"init() done. cleaner location : {CLEANER_LOC}")


# 1. 미세 먼지 확산
def diffuse_dust():
    global room

    new_room = [[0]*C for _ in range(R)]

    def diffuse_one():
        if room[r][c] == 0:
            return
        original_dust = room[r][c]
        # 인접 방향에 공기청정기가 있거나, 칸이 없으면 확산 X
        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nr, nc = r + dr, c + dc
            # board[r][c] // 5 만큼 확산된다.
            if 0 <= nr < R and 0 <= nc < C and [nr, nc] not in CLEANER_LOC:
                new_room[nr][nc] += original_dust // 5
                room[r][c] -= original_dust // 5
        new_room[r][c] += room[r][c]

    # 동시에 발생
    for r in range(R):
        for c in range(C):
            # 공기 청정기 자리면 continue
            if [r, c] in CLEANER_LOC:
                new_room[r][c] = -1
                continue
            diffuse_one()

    room = new_room
    print_debug(f"diffuse_dust() done.")


# 2. 공기청정기 작동
def operate_cleaner():

    # counter: True -> 시계, False -> 반시계
    def operate(counter: bool):
        global room

        direction_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # 위: 반시계, 아래: 시계
        if counter:
            change = 1
            start = CLEANER_LOC[1]
        else:
            change = -1
            start = CLEANER_LOC[0]

        curr_d = 0
        dr, dc = direction_list[curr_d]

        # 공기청정기에서 나오는 바람은 꺠끗한 바람
        prev_val = 0
        curr_r, curr_c = start[0] + dr, start[1] + dc

        # 공기청정기로 들어간 먼지는 정화된다.
        while [curr_r, curr_c] != start:
            # 1) 현재 값 저장
            curr_val = room[curr_r][curr_c]

            # 2) 이전 위치 값을 현재 위치에 저장
            room[curr_r][curr_c] = prev_val

            # 3) 이전 값 갱신
            prev_val = curr_val

            # 4) 현재 위치 갱신
            nr, nc = curr_r + dr, curr_c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                curr_d += change
                dr, dc = direction_list[curr_d]
                nr, nc = curr_r + dr, curr_c + dc
            curr_r, curr_c = nr, nc

    operate(True)
    operate(False)

    print_debug("operate_cleaner() done.")


# 1초 동안의 동작
def one_second():
    diffuse_dust()
    operate_cleaner()


def solution():
    init()

    for _ in range(T):
        one_second()

    return sum(map(sum, room)) + 2


def print_debug(title=""):
    if not DEBUG:
        return

    print("=============================")
    print(title)
    for r in range(R):
        for c in range(C):
            print(f"{room[r][c]:4}", end="")
        print()
    print("=============================")


# === output ===
DEBUG = False
# DEBUG = True
# ans: T초 후에 남은 미세 먼지의 양
print(solution())
