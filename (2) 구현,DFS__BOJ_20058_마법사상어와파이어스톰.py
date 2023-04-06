# (2) 구현,DFS__BOJ_20058_마법사상어와파이어스톰
# 1. 시간 초과 -> list copy 최소화, O(2N) -> O(N)으로 해결 2. 파이썬도 함수 호출 많이 하면 성능 저하 되는구나. 3.(r, c) 자동완성 사용해서 바뀜 주의

# 1차 list slicing + O(n^2)       (4860)
# 2차 어레이 복사 (O(2n^2))          (시간 초과)
# 3차 (2차 함수 호출 버전)            (시간 초과)
# 4차 zip + 함수호출                (4988)
# 5차 일회성 코드 함수 호출로 변경       (4956)
# 6차 check 함수 inline 변경        (4328)
# 7차 map, sum 안 써 봄             (4992)
# 8차 bfs->dfs                   (4960)
# 9차 check 함수 2개 다 inline      (3436)
# 10차 함수 호출 줄여봄                (3352)

from collections import deque

# ===input===
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))
EDGE = 2**N


# ===algorithm===
def print_2d_array(array_2d, e=EDGE):
    print("============")
    for r in range(e):
        for c in range(e):
            print(array_2d[r][c], end=' ')
        print()
    print("============")
    print()


direction_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# def check_boundary(index_row, index_col):
#     return 0 <= index_row < EDGE and 0 <= index_col < EDGE
# def check_ice(arr, index_row, index_col):
#     return arr[index_row][index_col] > 0


# 1. L 단계 파이어스톰
def firestorm(arr, level):

    stride = 2 ** level
    # def rotate_2d_array(start_r, start_c):
    #     copied_arr = [lst[start_c:start_c+stride] for lst in arr[start_r:start_r+stride]]
    #     transposed_arr = list(zip(*copied_arr))
    #
    #     for tr in range(stride):
    #         arr[start_r+tr][start_c:start_c+stride] = transposed_arr[tr][::-1]
    # def melt_ice():
    #     melted_list = []
    #     for r in range(EDGE):
    #         for c in range(EDGE):
    #             adj_ice = 0
    #             for dr, dc in direction_list:
    #                 nr, nc = r + dr, c + dc
    #                 # 6차 inline 버전
    #                 if check_boundary(nr, nc) and arr[nr][nc] > 0: #check_ice(arr, nr, nc):
    #                     adj_ice += 1
    #             if adj_ice < 3 and arr[r][c] > 0:
    #                 melted_list.append((r, c))
    #     for melt_r, melt_c in melted_list:
    #         arr[melt_r][melt_c] -= 1

    # 1. 격자를 2^L 2^L로 나눈다:
    # 2. 모든 부분 격자를 시계 방향 90도 회전시킨다.
    for area_r in range(0, EDGE, stride):
        for area_c in range(0, EDGE, stride):
            copied_arr = [lst[area_c:area_c + stride] for lst in arr[area_r:area_r + stride]]
            for small_area_r in range(stride):
                for small_area_c in range(stride):
                    arr[area_r+small_area_r][area_c+small_area_c] = copied_arr[stride-1-small_area_c][small_area_r]
            '''
            new_arr = [[0]*stride for _ in range(stride)]
            for r in range(stride):
                for c in range(stride):
                    new_arr[c][stride-r-1] = arr[board_r][board_c]
            for r in range(stride):
                for c in range(stride):
                    board_r, board_c = area_r+r, area_c+c
                    arr[board_r][board_c] = new_arr[r][c]
                    # arr[r][c] = copied_arr[stride-small_area_c-1][small_area_r] '''

    # 3. 3개 이상의 얼음 칸과 인접해 있지 않은 칸은 얼음의 양이 1 줄어든다.
    melted_list = []
    for r in range(EDGE):
        for c in range(EDGE):
            adj_ice = 0
            for dr, dc in direction_list:
                nr, nc = r+dr, c+dc
                if 0 <= nr < EDGE and 0 <= nc < EDGE and arr[nr][nc] > 0:    # check_ice(arr, nr, nc):
                    adj_ice += 1
            if adj_ice < 3 and arr[r][c] > 0:
                melted_list.append((r, c))
    for melt_r, melt_c in melted_list:
        arr[melt_r][melt_c] -= 1


# 2. 총합
def sum_of_ice(array_2d):
    return sum(list(map(sum, array_2d)))


# 3. 가장 큰 덩어리 BFS -> stack
def get_max_ice(array_2d) -> int:
    breadth = 0

    # 2개 자료 구조
    visited = [[False] * EDGE for _ in range(EDGE)]

    def dfs(start_r, start_c) -> int:
        ret = 0
        will_be_vistied_queue = deque()

        will_be_vistied_queue.append((start_r, start_c))
        visited[start_r][start_c] = True
        ret += 1

        # queue
        while will_be_vistied_queue:
            curr_r, curr_c = will_be_vistied_queue.pop()
            for dr, dc in direction_list:
                next_r, next_c = curr_r+dr, curr_c+dc
                if 0 <= next_r < EDGE and 0 <= next_c < EDGE and not visited[next_r][next_c] and array_2d[next_r][next_c] > 0:  #check_ice(array_2d, next_r, next_c):
                        will_be_vistied_queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        ret += 1
        return ret

    for r in range(EDGE):
        for c in range(EDGE):
            if array_2d[r][c] > 0 and not visited[r][c]:
                breadth = max(breadth, dfs(r, c))

    return breadth


# ===output===
for lv in L:
    firestorm(A, lv)

print(sum_of_ice(A))
print(get_max_ice(A))
