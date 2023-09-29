# (0.5, 골2) BOJ_19238_스타트택시

# 손님을 도착지로 데려줄 때마다 연료가 충전됨
# 연료가 바닥나면 그 날의 업무가 끝남

# M명의 승객을 태우는 것이 목표임
# N*N grid [EMPTY, WALL]

# 인접 빈 칸 중 하나로 이동
# 항상 최단 경로로만 이동한다.

# 승객
# 1. 빈 칸 중 하나에 서 있다.
# 2. 다른 빈 칸 중 하나로 이동하려고 한다.
# 3. 여러 승객이 같이 탐승하는 경우는 없다.

# 택시 태우기
# 1. 현 위치에서 최단 거리가 가장 짧은 승객 선택
# 2. 여러 명이명 min(r), min(c)
# 3. dst 성공적으로 이동시키면, 소모한 연료 양의 두배가 충전된다.
# 4. 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.

from collections import deque
import heapq


# === input ===
taxi = [0, []]
OIL, LOC = 0, 1                 # for taxi
EMPTY, WALL = 0, 1              # for grid

N, M, taxi[OIL] = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
taxi[LOC] = list(map(lambda x: int(x) - 1, input().split()))
dst_dict = dict()


# === algorithm ===
def init():
    global grid, dst_dict

    for passenger_id in range(1, M + 1):
        src_r, src_c, dst_r, dst_c = map(lambda x: int(x) - 1, input().split())
        grid[src_r][src_c] = -1 * passenger_id
        dst_dict[passenger_id] = [dst_r, dst_c]


# return: 도착에 성공하면 True
def go_to_passenger() -> bool:
    global taxi

    def bfs():

        possible_pq = []            # (거리, r, c)

        queue = deque([taxi[LOC]])
        distance = [[-1] * N for _ in range(N)]
        distance[taxi[LOC][0]][taxi[LOC][1]] = 0

        while queue:
            r, c = queue.popleft()
            dist = distance[r][c]

            # 가능한 위치가 있고, 가능한 위치보다 거리가 큰 경우
            if possible_pq and possible_pq[0][0] < dist:
                break

            # oil 이 모자르는 경우
            if taxi[OIL] < dist:
                break

            # 승객이 있는 경우
            if grid[r][c] < 0:
                heapq.heappush(possible_pq, (dist, r, c))



            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != WALL and distance[nr][nc] == -1:
                    queue.append([nr, nc])
                    distance[nr][nc] = dist + 1
        if possible_pq:
            return possible_pq[0]
        else:
            return None

    taxi_info = bfs()
    if not taxi_info:
        return False
    else:
        # 택시 이동
        path, next_r, next_c = taxi_info
        taxi[OIL] -= path
        taxi[LOC] = [next_r, next_c]
        return True


# return: 도착에 성공하면 True
def go_to_destination() -> bool:
    global grid, dst_dict, taxi

    passenger_id = -1 * grid[taxi[LOC][0]][taxi[LOC][1]]

    # TODO: 도착에 성공하면 grid, dst_dict에서 삭제
    def bfs():

        queue = deque([taxi[LOC]])
        distance = [[-1] * N for _ in range(N)]
        distance[taxi[LOC][0]][taxi[LOC][1]] = 0

        while queue:
            r, c = queue.popleft()
            dist = distance[r][c]

            # oil 이 모자르는 경우
            if taxi[OIL] < dist:
                break

            # 도착한 경우
            if [r, c] == dst_dict[passenger_id]:
                return [dist, r, c]

            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != WALL and distance[nr][nc] == -1:
                    queue.append([nr, nc])
                    distance[nr][nc] = dist + 1

        return []

    taxi_info = bfs()
    if not taxi_info:
        return False
    else:
        # 택시 이동
        path, next_r, next_c = taxi_info

        grid[taxi[LOC][0]][taxi[LOC][1]] = EMPTY

        taxi[OIL] -= path
        taxi[OIL] += 2*path
        taxi[LOC] = [next_r, next_c]
        del dst_dict[passenger_id]

        return True


def solution():
    init()

    while dst_dict:
        if not go_to_passenger():
            break
        print_debug("after go src")
        if not go_to_destination():
            break
        print_debug("after go dst")
    return -1 if dst_dict else taxi[OIL]


def print_debug(title=""):

    if not DEBUG:
        return

    print("=====================================")
    print(title)
    print(f"taxi oil: {taxi[OIL]}")

    for r in range(N):
        for c in range(N):
            if [r, c] == taxi[LOC]:
                print("ㅁ", end="")
                continue
            if grid[r][c] == EMPTY:
                print(f"_", end="")
            elif grid[r][c] == WALL:
                print(f"|", end="")
            else:
                print(f"{-1*grid[r][c]:1}", end="")
        print()
    print("=====================================")

# === output ===
DEBUG = False
# DEBUG = True
print(solution())
