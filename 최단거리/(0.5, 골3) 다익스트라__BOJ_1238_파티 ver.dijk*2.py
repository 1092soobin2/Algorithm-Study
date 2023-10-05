# (0.5, 골3) BOJ_1238_파티


# N student
# X번 마을에 모여서 파티
# M개 단방향 도로
# i 번쨰 길은 T_i 시간 소요됨

from collections import deque


# === in ===
N, M, X = map(int, input().split())
adj_list1 = [list() for _ in range(N)]
adj_list2 = [list() for _ in range(N)]


# === alg ===
def init():
    global adj_list1, adj_list2, X

    X -= 1
    for _ in range(M):
        start, end, time = map(int, input().split())
        adj_list1[start - 1].append([end - 1, time])
        adj_list2[end - 1].append([start - 1, time])


def dijkstra(start, to_X):

    if to_X:
        adj_list = adj_list1
    else:
        adj_list = adj_list2

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

    dijkstra_to_X = dijkstra(X, True)
    dijkstra_from_X = dijkstra(X, False)

    possible_dist = [dijkstra_to_X[i] + dijkstra_from_X[i] for i in range(N)]

    return max(possible_dist)



# === out ===
print(solution())
