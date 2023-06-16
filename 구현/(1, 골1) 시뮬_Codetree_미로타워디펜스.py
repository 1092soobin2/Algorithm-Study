# (1, 골1) 시뮬_Codetree_미로타워디펜스

# n*n board

# monster (1, 2, 3)


# === input ===
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
attack_list = [list(map(int, input().split())) for _ in range(M)]


# === algorithm ===
loc_list = []           # 나선형 구조 위치 리스트


def init_loc_list():
    global loc_list
    direction_list = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    repeat = 2

    # start
    r, c, d = N // 2, N // 2, 0

    # go
    for forward in range(1, N):
        if forward == N - 1:
            repeat = 3
        # change direction
        for _ in range(repeat):
            # go forward
            dr, dc = direction_list[d]
            for _ in range(forward):
                r, c = r + dr, c + dc
                loc_list.append([r, c])
            d = (d + 1) % 4


# 1. 공격
def attack(direction, intensity) -> int:
    global board

    ret_int = 0         # score, sum of monster number
    direction_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    r, c = N // 2, N // 2
    dr, dc = direction_list[direction]
    for _ in range(intensity):
        r, c = r + dr, c + dc
        ret_int += board[r][c]
        board[r][c] = 0

    print_debug(f"attack done, direction: {direction}, intensity: {intensity}")

    return ret_int


# 2. 몬스터 이동. 빈 칸 채우기
def fill():
    global board

    empty_idx = 0
    for monster_r, monster_c in loc_list:
        # 채워져 있으면 옮겨주기
        if board[monster_r][monster_c] != 0:
            # 몬스터 이동
            empty_r, empty_c = loc_list[empty_idx]
            if [empty_r, empty_c] != [monster_r, monster_c]:
                board[empty_r][empty_c] = board[monster_r][monster_c]
                board[monster_r][monster_c] = 0
            empty_idx += 1

    print_debug("fill done")


# 3(반복). 4번 이상 같은 종류면 삭제하고 채우기
def remove_4():
    global board

    ret_int = 0

    while True:
        deleted = 0
        acc = 1
        for now_loc_idx in range(1, N*N - 1):
            r, c = loc_list[now_loc_idx]
            prev_r, prev_c = loc_list[now_loc_idx - 1]
            if board[r][c] == board[prev_r][prev_c]:    # 같으면 acc + 1하고 지나 가기
                acc += 1
            else:                                       # 다르면 삭제 혹은 지나 가기
                if acc >= 4:
                    deleted += acc * board[prev_r][prev_c]
                    for i in range(1, acc + 1):
                        same_loc_idx = now_loc_idx - i
                        sr, sc = loc_list[same_loc_idx]
                        board[sr][sc] = 0
                # 새롭게 세어 주기
                acc = 1
        print_debug(f"remove done")

        if deleted == 0:
            break
        ret_int += deleted

        fill()

    return ret_int


# 4. 짝 지어서 채우기 (개수, 숫자)
def fill_again():
    global board

    new_board = [[0]*N for _ in range(N)]

    # 세기
    empty_idx = 0
    acc = 1
    for now_loc_idx in range(1, N * N - 1):
        r, c = loc_list[now_loc_idx]
        prev_r, prev_c = loc_list[now_loc_idx - 1]
        # 빈 칸이면 세지 않는다.
        if board[prev_r][prev_c] == 0:
            break
        if board[r][c] == board[prev_r][prev_c]:  # 같으면 acc + 1하고 지나 가기
            acc += 1
        else:
            empty_r, empty_c = loc_list[empty_idx]
            new_board[empty_r][empty_c] = acc
            empty_r, empty_c = loc_list[empty_idx + 1]
            new_board[empty_r][empty_c] = board[prev_r][prev_c]
            acc = 1
            empty_idx += 2
            if empty_idx >= (N * N - 1):
                break

    board = new_board
    print_debug("fill_again done")


# 5. 점수: 몬스터 번호 * 몬ㄴ스터 개수


def print_debug(title=""):
    if not DEBUG:
        return

    print("====================")
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{board[r][c]:4}", end ="")
        print()
    print("====================")


# === output ===
init_loc_list()

DEBUG = False
ans = 0
for attack_arg in attack_list:
    ans += attack(*attack_arg)
    fill()
    ans += remove_4()
    fill_again()

print(ans)
