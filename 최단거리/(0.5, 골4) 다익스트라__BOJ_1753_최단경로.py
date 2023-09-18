# (0.5, 골4) BOJ_1753_최단경로

# 방향 그래프가 주어지면 주어진 시작점에서
# 다른 모든 정점으로의 최단 경로를 구하는 프로그램

import heapq
import sys

input = sys.stdin.readline


# === input ===
INF = 1e9
VERTEX, EDGE = map(int, input().split())
START = int(input())
# NEXT_VERTEX, WEIGHT = 0, 1                  # for adj_graph access
adj_graph = [list() for _ in range(VERTEX + 1)]
for _ in range(EDGE):
    u, v, w = map(int, input().split())     # u -> v
    adj_graph[u].append([v, w])


# === algorithm ===
def dijkstra():

    pq = []
    distance = [INF] * (VERTEX + 1)

    # start
    distance[START] = 0
    heapq.heappush(pq, [distance[START], START])

    while pq:
        curr_distance, curr_vertex = heapq.heappop(pq)

        if distance[curr_vertex] < curr_distance:
            continue

        for next_vertex, weight in adj_graph[curr_vertex]:
            if distance[next_vertex] > curr_distance + weight:
                distance[next_vertex] = curr_distance + weight
                heapq.heappush(pq, [distance[next_vertex], next_vertex])

    return distance


# === output ===
answer = dijkstra()
for i in range(1, VERTEX + 1):
    print(answer[i] if answer[i] != INF else "INF")