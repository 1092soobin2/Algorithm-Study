# (1, 골4) Codetree_바이러스백신


# N*N board
# 병원 X, 벽X 모든 지역에 바이러스가 생김

# M개의 병원을 골라서
# 인접칸으로 백신 공금

from collections import deque

# === input ===
N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]
hospital_list = []


# === algorithm ===
MAX = 1e9


def init():
    global hospital_list

    for r in range(N):
        for c in range(N):
            if BOARD[r][c] == 2:
                hospital_list.append([r, c])

    if DEBUG:
        print("hospital list: ", hospital_list)


# n Combination r 의 결과를 반환
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

    if DEBUG:
        print("comb(): ", ret_list)
    return ret_list


# M개의 병원이 주어졌을 때, 바이러스 제거 최소 시간을 반환
def bfs(start_list) -> int:
    ret_int = 0

    queue = deque()
    visited = [[-1]*N for _ in range(N)]

    for r, c in start_list:
        queue.append([r, c])
        visited[r][c] = 0

    ret_int = 0
    while queue:
        curr_r, curr_c = queue.popleft()
        curr_visited = visited[curr_r][curr_c]
        if BOARD[curr_r][curr_c] == 2:
            ret_int = max(curr_visited - 1, ret_int)
        else:
            ret_int = curr_visited

        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nr, nc = curr_r + dr ,curr_c + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if BOARD[nr][nc] == 0 or BOARD[nr][nc] == 2:
                    queue.append([nr, nc])
                    visited[nr][nc] = curr_visited + 1

    for r in range(N):
        for c in range(N):
            if BOARD[r][c] == 0 and visited[r][c] == -1:
                return MAX

    return ret_int


# === output ===
# ans: 바이러스를 전부 없애는 데 걸리는 시간 중 최소 시간

DEBUG = False

ans = MAX
init()
for m_hospital_list in comb(hospital_list, M):
    ans = min(ans, bfs(m_hospital_list))
print(ans if ans != MAX else -1)
