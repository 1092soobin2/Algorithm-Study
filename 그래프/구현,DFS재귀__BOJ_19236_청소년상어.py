# 구현,DFS__BOJ_19236_청소년상어

import copy
# ===input===
DIRECTION_TUP = ((-1, 1),\
                 (-1, 0), (-1, -1), (0, -1), (1, -1), \
                 (1, 0), (1, 1), (0, 1), (-1, 1))
INVALID_FISH_NUM = -1

# 위치, 방향을 관리한다.
space = []
for i in range(4):
    space.append(list())
    tmp_list = list(map(int, input().split()))
    for j in range(4):
        n, d = tmp_list[2 * j], tmp_list[2 * j + 1]
        space[i].append([n, d])


def print_space(array):
    print("==========================")
    for i in range(4):
        for j in range(4):
            print(f"{array[i][j][0]}/{array[i][j][1]} ", end='')
        print()
    print("==========================\n")


# ===algorithm===
def move_fishes(array, sr, sc):
    for number in range(1, 17):
        # Find fish location.
        from_r, from_c = -1, -1
        for i in range(4):
            for j in range(4):
                if array[i][j][0] == number:
                    from_r, from_c = i, j
        if from_r == -1:
            continue
        # Move fish
        for dir_id in range(8):
            next_dir_id = (array[from_r][from_c][1] + dir_id) % 8
            dr, dc = DIRECTION_TUP[next_dir_id]
            to_r, to_c = from_r + dr, from_c + dc
            if 0 <= to_r < 4 and 0 <= to_c < 4 and not (sr == to_r and sc == to_c):
                # array[from_r][from_c], array[to_r][to_c] = array[to_r][to_c], array[from_r][from_c]
                array[from_r][from_c][0], array[to_r][to_c][0] = array[to_r][to_c][0], array[from_r][from_c][0]
                array[from_r][from_c][1], array[to_r][to_c][1] = array[to_r][to_c][1], next_dir_id
                break


# (r, c) 방문
def dfs(array, r, c, total_fish_number):

    global ans
    array = copy.deepcopy(array)

    def get_possible_shark_position():
        possible_pos_list = []

        dr, dc = DIRECTION_TUP[array[r][c][1]]

        r2, c2 = r, c
        for _ in range(4):
            r2, c2 = r2+dr, c2+dc
            if 0 <= r2 < 4 and 0 <= c2 < 4:
                if array[r2][c2][0] != INVALID_FISH_NUM:
                    possible_pos_list.append((r2, c2))
            else:
                break
        return possible_pos_list

    # 1. 물고기 먹기
    curr_fish_number = array[r][c][0]
    array[r][c][0] = INVALID_FISH_NUM
    total_fish_number += curr_fish_number
    ans = max(ans, total_fish_number)

    # 2. 물고기 이동
    move_fishes(array, r, c)

    # 3. 상어 이동
    positions = get_possible_shark_position()
    for nr, nc in positions:
        # print(f"shark {r},{c} -> {nr},{nc} in {positions}")
        # print(f"curr total: {total_fish_number}")
        # print_space(array)
        dfs(array, nr, nc, total_fish_number)


# ===output===
ans = 0
shark_r, shark_c = 0, 0
dfs(space, shark_r, shark_c, 0)
print(ans)
