# (0.5, 골3) BOJ_1238_파티


# N student
# X번 마을에 모여서 파티
# M개 단방향 도로
# i 번쨰 길은 T_i 시간 소요됨

from collections import deque
import heapq


# === in ===
N, M, X = map(int, input().split())
adj_list = [list() for _ in range(N)]


# === alg ===
def init():
    global adj_list, X

    X -= 1
    for _ in range(M):
        start, end, time = map(int, input().split())
        adj_list[start - 1].append([end - 1, time])


def dijkstra(start):
    inf = 1e9
    dijkstra_dist = [inf] * N

    queue = deque([start])
    dijkstra_dist[start] = 0

    while queue:
        curr_vertex = queue.popleft()
        curr_time = dijkstra_dist[curr_vertex]

        for next_vertex, time in adj_list[curr_vertex]:
            if dijkstra_dist[next_vertex] > curr_time + time:
                dijkstra_dist[next_vertex] = curr_time + time
                queue.append(next_vertex)

    return dijkstra_dist


def solution():
    init()

    dijkstra_matrix = [dijkstra(i) for i in range(N)]

    possible_dist = [dijkstra_matrix[i][X] + dijkstra_matrix[X][i] for i in range(N)]

    return max(possible_dist)



# === out ===
print(solution())
