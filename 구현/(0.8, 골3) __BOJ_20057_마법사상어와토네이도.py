# (0.8, 골3) __BOJ_20057_마법사상어와토네이도

# N×N grid [sand]

# torando
# 1. 격자의 가운데 칸부터 토네이도의 이동이 시작된다.
# 2. 한 번에 한 칸 이동
    # 비율 칸:  y에 있는 모래의 해당 비율
    # α: 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
# 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.

# ans: 격자의 밖으로 나간 모래의 양을 구해보자.

# === input ===
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
def get_loc_list() -> list:
    direction_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    ret_list = []

    # 11 22 33 44 55 666
    repeat = 2
    direction_idx = 1
    r, c = N // 2, N // 2   # start index
    ret_list.append([r, c])

    for forward in range(1, N):

        # If N-1 th order, then repeat number is 3.
        if forward == N - 1:
            repeat = 3

        # Repeat.
        for _ in range(repeat):
            dr, dc = direction_list[direction_idx]      # Get direction
            direction_idx = (direction_idx + 1) % 4     # Change direction

            # Go forward.
            for _ in range(forward):
                r, c = r + dr, c + dc
                ret_list.append([r, c])
    return ret_list


def spread_sand(curr_loc, next_loc):

    def spread_some_sand(dst_loc_list, percent) -> int:
        global A

        out_sand = 0

        # Get sand volume to be moved.
        if percent == 1:
            move_sand = A[r2][c2]
        else:
            move_sand = int(backup_src_sand * percent)

        for r, c in dst_loc_list:
            # Move sand to destination.
            if 0 <= r < N and 0 <= c < N:
                A[r][c] = A[r][c] + move_sand
            else:
                out_sand = out_sand + move_sand

            # Remove from source.
            A[r2][c2] -= move_sand

        return out_sand

    [r1, c1], [r2, c2] = curr_loc, next_loc
    backup_src_sand = A[r2][c2]                    # Backup source sand.

    # forward direction
    dr, dc = r2 - r1, c2 - c1
    # left, right direction
    [dr1, dc1], [dr2, dc2] = ([-1, 0], [1, 0]) if dr == 0 else ([0, -1], [0, 1])

    sum_of_out_sand = 0
    sum_of_out_sand += spread_some_sand([[r1 + dr1, c1 + dc1],               [r1 + dr2, c1 + dc2]],               0.01)
    sum_of_out_sand += spread_some_sand([[r1 + dr + dr1, c1 + dc + dc1],     [r1 + dr + dr2, c1 + dc + dc2]],     0.07)
    sum_of_out_sand += spread_some_sand([[r1 + dr + 2*dr1, c1 + dc + 2*dc1], [r1 + dr + 2*dr2, c1 + dc + 2*dc2]], 0.02)
    sum_of_out_sand += spread_some_sand([[r1 + 2*dr + dr1, c1 + 2*dc + dc1], [r1 + 2*dr + dr2, c1 + 2*dc + dc2]], 0.10)
    sum_of_out_sand += spread_some_sand([[r1 + 3*dr, c1 + 3*dc]],                                                 0.05)
    sum_of_out_sand += spread_some_sand([[r1 + 2*dr, c1 + 2*dc]],                                                 1)

    return sum_of_out_sand


def tornado():

    total_out_sand = 0

    loc_list = get_loc_list()

    for i in range(N * N - 1):
        curr_loc, next_loc = loc_list[i], loc_list[i + 1]
        total_out_sand += spread_sand(curr_loc, next_loc)

        print_deubg(f"{curr_loc} -> {next_loc}")

    return total_out_sand


def print_deubg(title=""):
    if not DEBUB:
        return

    print("=========================")
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{A[r][c]:3}", end="")
        print()
    print("=========================")

DEBUB = False
# DEBUB = True
print(tornado())
