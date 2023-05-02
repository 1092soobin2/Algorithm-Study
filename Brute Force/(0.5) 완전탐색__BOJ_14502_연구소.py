

EMPTY, WALL, VIRUS = 0, 1, 2

# ===input===
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]


# ===algorithm===
def comb(arr, r):
    ret_list = []
    len_arr = len(arr)

    def dfs(start_i, acc):
        if len(acc) == r:
            ret_list.append(acc)
            return

        for i in range(start_i, len_arr):
            dfs(i + 1, acc + [arr[i]])

    dfs(0, [])
    return ret_list


def find_safety_area(arr):
    ret_area = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                ret_area += 1

    return ret_area


def infect_virus(arr):

    visited = [[False]*M for _ in range(N)]

    def bfs(start_loc):

        queue = [start_loc]
        visited[start_loc[0]][start_loc[1]] = True

        while queue:
            curr_r, curr_c = queue.pop(0)

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = curr_r+dr, curr_c+dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == EMPTY:
                    queue.append([nr, nc])
                    arr[nr][nc] = VIRUS
                    visited[nr][nc] = True

    for r in range(N):
        for c in range(M):
            if arr[r][c] == VIRUS and not visited[r][c]:
                bfs([r, c])


def install_wall(arr, wall_list) -> list:
    new_arr = [arr[r][:] for r in range(N)]
    for r, c in wall_list:

        new_arr[r][c] = WALL

    return new_arr


def sol():
    answer = 0
    loc_list = [[r, c] for c in range(M) for r in range(N)]

    for walls in comb(loc_list, 3):
        elem = list(map(lambda x: MAP[x[0]][x[1]], walls))
        if elem != [EMPTY]*3:
            continue
        wall_installed = install_wall(MAP, walls)
        infect_virus(wall_installed)
        answer = max(answer, find_safety_area(wall_installed))

    return answer


# ===output===
print(sol())
