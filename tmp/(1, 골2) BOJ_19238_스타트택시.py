# (0.5, 골2) BOJ_19238_스타트택시

# 손님을 도착지로 데려다 줄 때마다 연료 충천
# 연료가 바닥나면 그 날의 업무가 끝남.

# M명의 승객
# N*N grid [EMPTY, WALL]

# taxi
# 빈칸 -> 상하좌우 인접 칸 중 빈칸으로 이동 가능
# 항상 최단경로로만 이동

# passenger
# 빈칸 중 하나에 서 있다.
# 다른 빈칸 중 하나로 이동하려고 한다.
# 여러 승객이 같이 탐승하는 경우는 없다.


# 현재 위치에서 최단거리가 가장 짧은 승객을 고른다.
# 여러 명이면, min(r) -> min(c)

# 한 칸 이동 시마다, 연료 1 소모
# 목적지로 이동시키면, 소모한 연료 양의 2배가 충전된다.

# 이동 도중에 연료==0 이면 실패
# 목적지로 이동시킨 동시에 연료==0인 경우는 성공


from collections import deque
import heapq


# === input ===
N, M, oil = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
EMPTY, WALL = 0, 1
taxi_loc = list(map(lambda x: int(x) - 1, input().split()))
passenger_loc_dict = dict()
SRC, DST = 0, 1


# === algorithm ===
def init():
    global passenger_loc_dict, grid
    passenger_id = 2
    for _ in range(M):
        src_r, src_c, dst_r, dst_c = map(lambda x: int(x) - 1, input().split())
        grid[src_r][src_c] = passenger_id
        passenger_loc_dict[passenger_id] = [[src_r, src_c], [dst_r, dst_c]]
        passenger_id += 1


# return: 이동에 성공하면 True 리턴
def go_to_passenger() -> bool:
    global taxi_loc, oil

    def bfs():

        possible_loc = []  # [거리, r, c, id]
        possible_path = 0
        queue = deque([taxi_loc])
        visited = [[-1] * N for _ in range(N)]
        visited[taxi_loc[0]][taxi_loc[1]] = 0

        while queue:
            curr_r, curr_c = queue.popleft()
            curr_v = visited[curr_r][curr_c]

            if possible_loc and possible_path < curr_v:
                return grid[possible_loc[0]][possible_loc[1]], possible_path

            if grid[curr_r][curr_c] > WALL:
                if not possible_loc:
                    possible_loc = [curr_r, curr_c]
                    possible_path = curr_v
                else:
                    if possible_path == curr_v:
                        if possible_loc[0] > curr_r:
                            possible_loc = [curr_r, curr_c]
                        elif possible_loc[0] == curr_r and possible_loc[1] > curr_c:
                            possible_loc = [curr_r, curr_c]

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != WALL and visited[nr][nc] == -1:
                    queue.append([nr, nc])
                    visited[nr][nc] = curr_v + 1

        return None, None

    passenger_id, path = bfs()
    if not path:
        return False
    if oil >= path:
        taxi_loc = passenger_loc_dict[passenger_id][SRC]
        oil -= path
        return True
    else:
        return False


def go_to_dst() -> bool:
    global grid, passenger_loc_dict, taxi_loc, oil

    passenger_id = grid[taxi_loc[0]][taxi_loc[1]]

    def bfs():

        queue = deque([taxi_loc])
        visited = [[-1] * N for _ in range(N)]
        visited[taxi_loc[0]][taxi_loc[1]] = 0

        while queue:
            curr_r, curr_c = queue.popleft()
            curr_v = visited[curr_r][curr_c]
            if [curr_r, curr_c] == passenger_loc_dict[passenger_id][DST]:
                return curr_v

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != WALL and visited[nr][nc] == -1:
                    queue.append([nr, nc])
                    visited[nr][nc] = curr_v + 1
        return None

    path = bfs()
    if not path:
        return False
    if oil >= path:
        grid[taxi_loc[0]][taxi_loc[1]] = EMPTY
        taxi_loc = passenger_loc_dict[passenger_id][DST]
        oil -= path
        oil += 2*path
        del passenger_loc_dict[passenger_id]
        return True
    else:
        return False


def solution():
    init()
    while passenger_loc_dict:
        if not go_to_passenger():
            return -1
        if not go_to_dst():
            return -1

    return oil


# === output ===
print(solution())
