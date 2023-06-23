# (1.2, 골2) Codetree_자율주행전기차

# n * n grid
# WALL
# m passenger
# 주어진 배터리 용량으로 승객을 모두 태워줄 수 있는

# 한 칸 이동 -> 배터리 1 소모
# 승객이 목적지 -> 소모 배터리의 두 배만큼 충전
# 배터리 전부 소모 시, 즉시 종료 (승객 태우고 목적지 도착한 경우는 제외)



from collections import deque
import heapq

# === input ===
N, M, C = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]             # line 1 - N+1
WALL = 1

# 차의 정보 [위치, 에너지]
car_info = [list(map(lambda x: int(x) - 1, input().split())), C]        # line N+2
LOC, ENERGY = 0, 1
src_board = [[0]*N for _ in range(N)]   # 승객 출발지 정보가 담긴 보드 (각 승객의 src는 unique)
DST_LIST = [None] * (M + 1)             # 승객 목적지 정보



# === algorithm ===
def init():
    global src_board

    passenger = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    for i in range(M):
        src, dst = passenger[i][:2], passenger[i][2:]
        src_board[src[0]][src[1]] = i + 1
        DST_LIST[i + 1] = dst

    print_debug(f"init() done. DST_LIST: {DST_LIST}, car_info:{car_info}")


# 다음 승객 찾기 (도착하지 못하면 [-1, -1] 리턴)
def go_src() -> int:
    global car_info
    start = car_info[LOC]

    def bfs():

        loc_pq = []

        queue = deque([start])
        visited = [[-1] * N for _ in range(N)]
        visited[start[0]][start[1]] = 0


        # 승객 태우기
        # 최단 거리 승객
        # min(r)
        # min(c)
        while queue:
            r, c = queue.popleft()
            curr_visited = visited[r][c]

            # src에 도달하면 pq에 넣어주기
            if src_board[r][c] != 0:
                heapq.heappush(loc_pq, (curr_visited, r, c))
                continue

            # 도달 src가 있으면 비교하기
            if loc_pq:
                if curr_visited > loc_pq[0][0]:
                    break

            # 인접칸으로 전진
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and BOARD[nr][nc] != WALL and visited[nr][nc] == -1:
                    queue.append([nr, nc])
                    visited[nr][nc] = curr_visited + 1

        if loc_pq:
            return loc_pq[0]
        else:
            return 1e9, None, None

    src_distance, src_r, src_c = bfs()
    print_debug(f"go_src() done. start: {start} -> src: {src_r, src_c}")
    if src_distance <= car_info[ENERGY]:
        car_info = [[src_r, src_c], car_info[ENERGY] - src_distance]
        return True
    else:
        return False


# 목적지 찾기 (도착하지 못하면 -1 리턴)
def go_dst() -> int:
    global car_info, src_board
    start = car_info[LOC]

    def bfs():

        queue = deque([start])
        visited = [[-1] * N for _ in range(N)]
        visited[start[0]][start[1]] = 0

        while queue:
            r, c = queue.popleft()
            curr_visited = visited[r][c]

            if [r, c] == DST_LIST[src_board[start[0]][start[1]]]:
                return curr_visited, [r, c]

            # 인접칸으로 전진
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and BOARD[nr][nc] != WALL and visited[nr][nc] == -1:
                    queue.append([nr, nc])
                    visited[nr][nc] = curr_visited + 1

        return -1, None

    # 도착하면 src_board 에서 지우기
    dist, dst_loc = bfs()

    print_debug(f"go_dst() done. start: {start} -> dst: {dst_loc}, car_info: {car_info}")

    if dist == -1 or dist > car_info[ENERGY]:
        return False
    else:
        src_board[start[0]][start[1]] = 0
        car_info = [dst_loc, car_info[ENERGY] + dist]
        return True


def check_src_board():
    for r in range(N):
        for c in range(N):
            if src_board[r][c] != 0:
                return False
    return True


def print_debug(title=""):
    if not DEBUG:
        return

    print("===========================================")
    print(title)
    for r in range(N):
        print(*src_board[r])
    print("===========================================")

# === output ===
DEBUG = False
# DEBUG = True

# ans: 최종 잔여 배터리의 양
init()

ans = -1
while True:
    # 다음 승객 == -1이고, check_src_board이면 -1
    if go_src():
        # 목적지 도착 못 하면 -1
        if not go_dst():
            break
    else:
        if check_src_board():
            ans = car_info[ENERGY]      # 최종 잔여 배터리
        else:
            ans = -1                    # 도착 불가능
        break
print(ans)

