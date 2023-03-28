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


def print_space():
    for i in range(4):
        for j in range(4):
            print(f"{space[i][j][0]}/{space[i][j][1]} ", end='')
        print()


# ===algorithm===
def move_fishes(array, sr, sc):
    for number in range(1, 17):
        # 물고기 위치
        from_r, from_c = -1, -1
        for i in range(4):
            for j in range(4):
                if array[i][j][0] == number:
                    from_r, from_c = i, j
        if from_r != -1:
            for dir_id in range(8):
                next_dir_id = (array[from_r][from_c][1] + dir_id) % 8
                dr, dc = DIRECTION_TUP[next_dir_id]
                to_r, to_c = from_r + dr, from_c + dc
                if 0 <= to_r < 4 and 0 <= to_c < 4 and not (sr == to_r and sc == to_c):
                    # array[from_r][from_c], array[to_r][to_c] = array[to_r][to_c], array[from_r][from_c]
                    array[from_r][from_c][0], array[to_r][to_c][0] = array[to_r][to_c][0], array[from_r][from_c][0]
                    array[from_r][from_c][1], array[to_r][to_c][1] = array[to_r][to_c][1], next_dir_id
                    break


def get_possible_position(array, sr, sc):
    positions = []
    d_id = space[sr][sc][1]
    dr, dc = DIRECTION_TUP[d_id]
    for i in range(4):
        sr, sc = sr+dr, sc+dc
        if 0 <= sr < 4 and 0 <= sc < 4:
            if array[sr][sc][0] != INVALID_FISH_NUM:
                positions.append([sr, sc])
        else:
            break
    return positions


# (r, c) 방문
def dfs(array, r, c, total_fish_number):
    global ans
    array = copy.deepcopy(array)

    # 물고기 먹기
    curr_fish_number = array[r][c][0]
    array[r][c][0] = INVALID_FISH_NUM

    move_fishes(array, r, c)

    positions = get_possible_position(array, r, c)

    ans = max(ans, total_fish_number + curr_fish_number)
    for nr, nc in positions:
        dfs(array, nr, nc, total_fish_number + curr_fish_number)


# ===output===
ans = 0
print_space()
shark_r, shark_c = 0, 0
dfs(space, 0, shark_r, shark_c)
print(ans)
