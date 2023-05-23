# (2, 골2) 시뮬__Codetree_코드트리빵


import heapq
from collections import deque

# === input ===
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
convenient = [None] + [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
CAMP, WALL = 1, -1


# === algorithm ===
# 1번 -> 1분 출발, 2번 -> 2분에 출발, ... m번 -> m분에 출발
loc = [None]*(M + 1)
reached = [False]*(M + 1)


# 1. 모두 움직임
def move(time):
    global loc

    def move_one(ith) -> list:

        r, c = loc[ith]
        direction_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def bfs(start):

            queue = [start]
            visited = [[-1]*N for _ in range(N)]
            visited[start[0]][start[1]] = 0

            while queue:
                curr_r, curr_c = queue.pop(0)
                curr_v = visited[curr_r][curr_c]
                if [curr_r, curr_c] == convenient[ith]:
                    return curr_v

                for dr, dc in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                    next_r, next_c = curr_r + dr, curr_c + dc
                    if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == -1 and board[next_r][next_c] != WALL:
                        queue.append([next_r, next_c])
                        visited[next_r][next_c] = curr_v + 1

            return 1e9

        # 편의점 방향 최단거리로 1칸
        # 상 -> 좌 -> 우 -> 하 [[-1, 0], [0, -1], [0, 1], [1, 0]]
        loc_pq = []
        for d_id in range(4):
            nr, nc = r + direction_list[d_id][0], c + direction_list[d_id][1]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != WALL:
                heapq.heappush(loc_pq, (bfs([nr, nc]), d_id, [nr, nc]))

        return loc_pq[0][2]

    for i in range(1, min(time, M + 1)):
        if not reached[i]:
            loc[i] = move_one(i)


# 2. 편의점에 도착하면 멈춤, 이때부터 다른 사람들은 그 칸을 지나갈 수 없음
def check_after_move(time):
    global board, reached

    for i in range(1, min(time, M + 1)):
        if reached[i]:
            continue
        elif loc[i] == convenient[i]:
            reached[i] = True
            try:
                board[loc[i][0]][loc[i][1]] = WALL
            except:
                print(f"{__name__} n/a location")
                exit()


# 3. t분일 때, t번이 베이스캠프로 감
def go_base_camp(time):
    global loc, board
    # t <= m이면

    if time > M:
        return

    def bfs() -> list:

        # t번 사람은 dst와 가장 가까운 베이스 캠프로 간다.
        # 여러 개면, min r -> min c
        # 해당 캠프 칸은 지나 갈 수 없다.
        visited = [[-1]*N for _ in range(N)]
        queue = deque()

        dst = convenient[time]
        queue.append(dst)
        visited[dst[0]][dst[1]] = 0

        camp_pq = []
        while queue:
            r, c = queue.popleft()
            curr_v = visited[r][c]

            # CAMP면 pq에 넣어주기
            if board[r][c] == CAMP:
                heapq.heappush(camp_pq, (curr_v, [r, c]))
            # CAMP가 아니고, 아직 camp에 도달하지 않았으면 진행하기
            elif not camp_pq:
                for dr, dc in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1 and board[nr][nc] != WALL:
                        queue.append([nr, nc])
                        visited[nr][nc] = curr_v + 1
            # CAMP가 아닌데, camp에 도달했으면 멈추기

        return list(camp_pq[0][1])

    nr, nc = loc[time] = bfs()
    board[nr][nc] = WALL


def print_info():

    print(g_time)
    for i in range(1, M + 1):
        if not reached[i]:
            print(f" {i}, dst:{convenient[i]}", end=" / ")
    print()
    for r in range(N):
        for c in range(N):
            if [r, c] in loc:
                print(f" [{loc.index([r, c])}]", end="\t")
            elif [r, c] in convenient:
                print(f" !{convenient.index([r, c])}!", end='\t')
            else:
                print(f"{board[r][c]:4}", end="\t")
        print()
    print()


g_time = 0
debug = False
while reached[1:] != [True]*M:
    g_time += 1
    move(g_time)
    check_after_move(g_time)
    if g_time <= M:
        go_base_camp(g_time)
    if debug:
        print_info()

print(g_time)