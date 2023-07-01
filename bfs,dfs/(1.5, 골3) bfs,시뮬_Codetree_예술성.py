# (1.5, 골3) Codetree_예술성

# N*N grid [1~10]

from collections import deque

# === input ===
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < N


# 그룹 아이디 매핑 하기
# return : 2차원 배열, 그룹별 element 개수 리스트
def map_group() -> list:
    ret_list = [[0]*N for _ in range(N)]    # 방문 여부 체크 배열의 역할
    ret_list2 = [[0, 0]]                         # 그룹별 원소 개수 저장
    group_id = 1                            # 한 그룹 발견 시마다 1 증가

    def bfs(start):
        queue = deque([start])
        ret_list[start[0]][start[1]] = group_id
        ret_list2.append([grid[r][c], 0])

        while queue:
            curr_r, curr_c = queue.popleft()
            ret_list2[group_id][1] += 1

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, curr_c + dc
                if check_boundary(nr, nc) and ret_list[nr][nc] == 0 and grid[r][c] == grid[nr][nc]:
                    queue.append([nr, nc])
                    ret_list[nr][nc] = group_id

    for r in range(N):
        for c in range(N):
            if ret_list[r][c] == 0:
                bfs([r, c])
                group_id += 1

    print_debug(arr=ret_list, title="map_group(): 그룹 아이디 매핑하기 result:\n"
                                    f"그룹별 개수 리스트 : {ret_list2}")

    return ret_list, ret_list2


# 맞닿은 변 개수
# group_arr : 매핑된 그룹 아이디
# num_of_group : 그룹 개수
# return : 2차원 상삼각 배열
def get_close(group_arr: list, num_of_group) -> list:
    ret_list = [[0]*(num_of_group + 1) for _ in range(num_of_group + 1)]        # [작은 gid][큰 gid] 간의 맞닿은 변 개수를 구함

    for r in range(N):
        for c in range(N):
            # 맞닿은 변의 수 : num(옆에 다른 숫자 칸이 있는 칸)
            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if check_boundary(nr, nc) and grid[r][c] != grid[nr][nc]:
                    gid1, gid2 = group_arr[r][c], group_arr[nr][nc]
                    ret_list[min(gid1, gid2)][max(gid1, gid2)] += 1

    print_debug(arr=ret_list, title=f"get_close(group, group_num): 맞닿은 변의 개수 구하기.\n"
                                    f"group_num: {num_of_group}")
    return ret_list


# 1. 초기 조화로움
# close_arr : 맞닿은 변 개수 2차원 배열
# group_list : 그룹별 개수 리스트
# return : 현 격자의 예술 점수
def get_art_score(close_arr, group_info_list) -> int:
    ret_int = 0             # 예술 점수: sum(모든 그룹 쌍의 조화로움)

    group_num = len(group_info_list) - 1
    for gid1 in range(1, group_num + 1):
        for gid2 in range(gid1 + 1, group_num + 1):
            # 조화로움(a, b) = (a개수 + b개수) * (a숫자) * (b숫자) * (맞닿은 변의 수)
            ret_int += (group_info_list[gid1][1] + group_info_list[gid2][1]) *\
                        group_info_list[gid1][0] * group_info_list[gid2][0] * close_arr[gid1][gid2]

    print_debug(title=f"get_art_score(close_arr, group_info) : 총 예술 점수 구하기 {ret_int}")
    return ret_int


# 2. 회전
def rotate():
    global grid
    new_grid = [[0]*N for _ in range(N)]

    def rotate_counterwise():
        for r in range(N):
            new_grid[N // 2][r] = grid[r][N // 2]
        for c in range(N):
            new_grid[(N - 1) - c][N // 2] = grid[N // 2][c]

    def rotate_clockwise(left_up_r, left_up_c):

        for r in range(left_up_r, left_up_r + N // 2):
            for c in range(left_up_c, left_up_c + N // 2):
                nr, nc = r - left_up_r, c - left_up_c
                nr, nc = left_up_r + nc, left_up_c + (N//2 - 1) - nr
                new_grid[nr][nc] = grid[r][c]

    # 1. 십자 : 반시계
    rotate_counterwise()
    # 2. 나머지 4 구역 : 개별적으로 시계
    rotate_clockwise(0, 0)
    rotate_clockwise(0, N//2 + 1)
    rotate_clockwise(N//2 + 1, 0)
    rotate_clockwise(N//2 + 1, N//2 + 1)

    grid = new_grid
    print_debug(grid, title=f"rotate() done.")


def print_debug(arr=[], title=""):

    if not DEBUG:
        return

    print("=================================")
    print(title)
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            print(f"{arr[r][c]:3}", end="")
        print()
    print("=================================")


# ans: (초기 + 1회전 + 2회전 + 3회전)
def solution():
    ret_int = 0
    for _ in range(4):
        group_arr, group_info_list = map_group()
        close_arr = get_close(group_arr, len(group_info_list) - 1)
        ret_int += get_art_score(close_arr, group_info_list)
        rotate()
    return ret_int

# === output ===
DEBUG = False
# DEBUG = True
print(solution())
