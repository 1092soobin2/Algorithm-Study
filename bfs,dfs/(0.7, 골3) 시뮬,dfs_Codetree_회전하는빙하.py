# (0.7, 골3) Codetree_회전하는빙하

# 2^n * 2^n gird

# 좌측 상단 빙하 회전 -> 인접 격자들도 똑같은 크기만큼 회전


from collections import deque

# === input ===
N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
level_list = list(map(int, input().split()))


# === algorithm ===
# 2^N -> 2^L * 2^(N-L)
# 1. 회전
def rotate(lv):
    global grid

    if lv == 0:
        return

    # 레벨 L
    # 2^L * 2^L 만큼 격자 선택
    # 2^(L-1) * 2^(L-1) 만큼 잘라 4등분하여 회전
    for r in range(0, 2 ** N, 2 ** lv):
        for c in range(0, 2 ** N, 2 ** lv):
            stride = 2**(lv-1)
            tmp_grid = [grid[ir][c:c + stride] for ir in range(r, r + stride)]
            # 좌상단
            for ir in range(r, r + stride):
                grid[ir][c:c + stride] = grid[ir + stride][c:c + stride]
            # 좌하단
            for ir in range(r, r + stride):
                grid[ir + stride][c:c + stride] = grid[ir + stride][c + stride:c + 2*stride]
            # 우하단
            for ir in range(r, r + stride):
                grid[ir + stride][c + stride:c + 2 * stride] = grid[ir][c + stride:c + 2 * stride]
            # 우상단
            for ir in range(r, r + stride):
                grid[ir][c + stride:c + 2 * stride] = tmp_grid[ir - r][:]

    print_debug("rotate() done.")


# 2. 빙하에 속한 얼음이 녹음
def melt():
    global grid

    # 인접칸 3개 이상 얼음이 있는 경우는 녹지 않음.
    # 그렇지 않으면 -1
    new_grid = [[0]*(2 ** N) for _ in range(2 ** N)]

    for r in range(2 ** N):
        for c in range(2 ** N):
            adj_ice = 0

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and grid[nr][nc] > 0:
                    adj_ice += 1
            if adj_ice >= 3:
                new_grid[r][c] = grid[r][c]
            else:
                new_grid[r][c] = max(grid[r][c] - 1, 0)

    grid = new_grid

    print_debug("melt() done.")


def print_debug(title=""):
    if not DEBUG:
        return

    print("============================")
    print(title)
    for r in range(2 ** N):
        for c in range(2 ** N):
            print(f"{grid[r][c]:4}", end="")
        print()
    print("============================")


def get_total_ice():
    return sum(map(sum, grid))


def get_largest_ice():

    ret_ice = 0

    visited = [[False]*(2 ** N) for _ in range(2 ** N)]

    def dfs(start):

        ret_int = 1     # 넓이

        stack = [start]
        visited[start[0]][start[1]] = True

        while stack:
            curr_r, curr_c = stack.pop()
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and grid[nr][nc] > 0 and not visited[nr][nc]:
                    stack.append([nr, nc])
                    visited[nr][nc] = True
                    ret_int += 1

        return ret_int

    for r in range(2 ** N):
        for c in range(2 ** N):
            if not visited[r][c] and grid[r][c] > 0:
                ret_ice = max(ret_ice, dfs([r, c]))

    return ret_ice


# === output ===
# 빙하의 총 양, 가장 큰 얼음 군집 크기
DEBUG = False
for level in level_list:
    rotate(level)
    melt()

print(get_total_ice())
print(get_largest_ice())
