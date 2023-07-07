# (1, 골5) Codetree_토스트계란틀 35

# n*n grid
# 4개선 분리 가능



from collections import deque

# === input ===
N, L, R = map(int, input().split())
mold = [list(map(int, input().split())) for _ in range(N)]
partition = [[[True, True] for _ in range(N)] for _ in range(N)]    # [아래, 오른쪽]


# === algorithm ===

# 1. 분리
# return : 분리 되었는지의 여부
def divide() -> bool:
    global partition
    ret_bool = False

    partition = [[[True, True] for _ in range(N)] for _ in range(N)]    # [아래, 오른쪽]

    for r in range(N):
        for c in range(N):
            for dr, dc in [[0, 1], [1, 0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    # L <= diff <= R 면 해당 선을 분리
                    if L <= abs(mold[r][c] - mold[nr][nc]) <= R:
                        partition[r][c][0 if r != nr else 1] = False
                        ret_bool = True

    print_debug("divide() done.")

    return ret_bool


# 2. 합치기
def conquer():

    # 분리된 칸들 합치기 -> sum // num
    visited = [[[False, False] for _ in range(N)] for _ in range(N)]

    def bfs(start):
        global mold

        egg_list = []
        egg_sum = 0
        egg_num = 0

        queue = deque([start])
        visited[start[0]][start[1]] = [True, True]

        while queue:
            curr_r, curr_c = queue.popleft()

            # 계란 합치기를 위한 정보들
            egg_list.append([curr_r, curr_c])
            egg_sum += mold[curr_r][curr_c]
            egg_num += 1

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    # (방문 X) && (벽 X)
                    if not visited[nr][nc][0 if curr_r != nr else 1] and not partition[min(curr_r, nr)][min(curr_c, nc)][0 if curr_r != nr else 1]:
                        queue.append([nr, nc])
                        visited[nr][nc] = [True, True]

        egg = egg_sum // egg_num
        for er, ec in egg_list:
            mold[er][ec] = egg

    for r in range(N):
        for c in range(N):
            if not visited[r][c][0]:
                bfs([r, c])

    print_debug("conquer() done.")


# ans: 계란의 이동이 몇 번 일어나는지
def solution():
    ans = 0

    while True:
        if not divide():
            break
        ans += 1
        conquer()

    return ans


def print_debug(title=""):
    if not DEBUG:
        return

    print("==========================")
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{mold[r][c]:4}", end="")
        print("\t\t", end="")
        for c in range(N):
            print(partition[r][c], end="")
        print()
    print("==========================")


# === output ===
DEBUG = False
# DEBUG = True
print(solution())