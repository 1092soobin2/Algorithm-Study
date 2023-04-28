# dfs__BOJ_21609_상어중학교

# NxN grid
# block : {black(-1), rainbow(0), ordinary(M)}

# === input ===
EDGE, NUM_OF_COLOR = map(int, input().split())
EMPTY = -2
BLACK, RAINBOW = -1, 0
board = [list(map(int, input().split())) for _ in range(EDGE)]


# === algorithm ===
def rotate_counterclockwise(arr: list) -> list:
    new_arr = [[0]*EDGE for _ in range(EDGE)]
    for r in range(EDGE):
        for c in range(EDGE):
            new_arr[EDGE - 1 - c][r] = arr[r][c]
    return new_arr


def gravity(arr: list):
    new_arr = [[EMPTY]*EDGE for _ in range(EDGE)]
    for c in range(EDGE):
        new_r = EDGE-1
        for r in range(EDGE-1, -1, -1):
            if arr[r][c] == BLACK:
                new_arr[r][c] = arr[r][c]
                new_r = r-1
            elif arr[r][c] != EMPTY:
                new_arr[new_r][c] = arr[r][c]
                new_r -= 1
    return new_arr


# block group: 연결 블록들 2개 이상
    # - 기준 블록: 무지개 블록이 아닌 블록 중, 행의 번호가 가장 작은 블록, 열의 번호가 가장 작은 블록
    # - 최소 하나의 일반 블록
    # - 일반 블록은 모두 같은색
    # - 검은색 X
    # - 무지개 O
def find_biggest_group(arr: list):
    ret_group = []
    num_rainbow = 0
    visited = [[False]*EDGE for _ in range(EDGE)]

    def dfs(start) -> list:
        ret_visited_list = []

        will_visited_stack = [start]
        visited[start[0]][start[1]] = True
        color = arr[start[0]][start[1]]
        rainbow_list = []

        while will_visited_stack:
            curr = will_visited_stack.pop()
            ret_visited_list.append(curr)

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = curr[0]+dr, curr[1]+dc
                if 0 <= nr < EDGE and 0 <= nc < EDGE:
                    if (arr[nr][nc] == RAINBOW or arr[nr][nc] == color) and not visited[nr][nc]:
                        will_visited_stack.append([nr, nc])
                        visited[nr][nc] = True
                        if arr[nr][nc] == RAINBOW:
                            rainbow_list.append([nr, nc])

        # rainbow는 깍두기, 복구
        for rr, rc in rainbow_list:
            visited[rr][rc] = False
        return [ret_visited_list, len(rainbow_list)]

    for r in range(EDGE):
        for c in range(EDGE):
            if arr[r][c] > 0 and not visited[r][c]:
                new_group, new_num_rainbow = dfs([r, c])
                if len(new_group) > len(ret_group) or\
                        (len(new_group) == len(ret_group) and new_num_rainbow >= num_rainbow):
                    ret_group = new_group
                    num_rainbow = new_num_rainbow

    if len(ret_group) == 1:
        ret_group.clear()
    return ret_group


def remove_group(arr, group: list) -> list:
    for r, c in group:
        arr[r][c] = EMPTY

    return arr


def print_arr(arr):
    for r in range(EDGE):
        line = " ".join(map(str, arr[r]))
        line = line.replace("-2", "_")
        print(line)


# === output ===
answer = 0

while True:
    # 1. 가장 큰 블록 그룹
    biggest_group = find_biggest_group(board)
    if not biggest_group:
        break
    # 2. 그룹 제거, B^2점 획득
    board = remove_group(board, biggest_group)
    answer += len(biggest_group) ** 2
    # 3. 중력 작용
    board = gravity(board)
    # 4. 90 반시계 회전
    board = rotate_counterclockwise(board)
    # 5. 중력 작용
    board = gravity(board)

print(answer)