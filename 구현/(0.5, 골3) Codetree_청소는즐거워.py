# (0.5, 골3) Codetree_청소는즐거워

# n*n (n is odd)

# 빗자루가 이동
# 이동 시마다 아래의 비율에 맞춰서 먼지가 이동
    # 이동 먼지는 기존의 양해 더해지고
    # 빗자루가 이동한 위치의 먼지는 다 없어짐
# a% = (원래 먼지량 -sum(다른 격자 이동량))


# === input ===
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
loc_list = []
DIRECTION_LIST = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 왼 아 오 위


# === algorithm ===
# 먼지의 이동
def move_dust(prev_loc, direction) -> int:
    global board

    ret_int = 0     # 격자 밖으로 나간 먼지 저장

    # 이동 위치와 퍼센트 저장
    r, c = prev_loc
    [dr0, dc0] = DIRECTION_LIST[direction]
    [dr1, dc1] = DIRECTION_LIST[(direction - 1) % 4]
    [dr2, dc2] = DIRECTION_LIST[(direction + 1) % 4]

    next_loc_list = [ [[r + dr1, c + dc1], 0.01], [[r + dr2, c + dc2], 0.01],
                      [[r + dr0 + dr1, c + dc0 + dc1], 0.07], [[r + dr0 + dr2, c + dc0 + dc2], 0.07],
                      [[r + dr0 + 2*dr1, c + dc0 + 2*dc1], 0.02], [[r + dr0 + 2*dr2, c + dc0 + 2*dc2], 0.02],
                      [[r + 2*dr0 + dr1, c + 2*dc0 + dc1], 0.10], [[r + 2*dr0 + dr2, c + 2*dc0 + dc2], 0.10],
                      [[r + 3*dr0, c + 3*dc0], 0.05]]
    a_loc = [r + 2*dr0, c + 2*dc0]
    next_loc = [r + dr0, c + dc0]

    original = board[next_loc[0]][next_loc[1]]
    for [nr, nc], proportion in next_loc_list:
        delta = int(original * proportion)      # 이동량
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] += delta
        else:
            ret_int += delta
        board[next_loc[0]][next_loc[1]] -= delta

    # a% 인 부분
    nr, nc = a_loc
    if 0 <= nr < N and 0 <= nc < N:
        board[nr][nc] += board[next_loc[0]][next_loc[1]]
    else:
        ret_int += board[next_loc[0]][next_loc[1]]

    # 다음 이동
    board[next_loc[0]][next_loc[1]] = 0

    print_debug()
    return ret_int


# 빗자루의 이동
def move_cleaner() -> int:

    ret_int = 0     # 격자 밖으로 나간 먼지 총량

    repeat = 2
    r, c, d = N // 2, N // 2, 0
    for forward in range(1, N):         # 앞으로 가는 횟수
        if forward == N - 1:
            repeat = 3
        for _ in range(repeat):         # 방향 바꾸기
            dr, dc = DIRECTION_LIST[d]
            for _ in range(forward):    # 앞으로 가기
                ret_int += move_dust([r, c], d)
                r, c = r + dr, c + dc
            d = (d + 1) % 4


    return ret_int


def print_debug():
    if not DEBUG:
        return

    print("--------------")

    for r in range(N):
        for c in range(N):
            print(f"{board[r][c]:4}", end="")
        print()
    print("--------------")


# === output ===
DEBUG = False
print(move_cleaner())
