import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

# input_edges = [list(map(int, input().split())) for _ in range(E)]
adj_list = [[] for _ in range(N+1)]    # [[node, dist], ... ]

# for node1, node2, dist in input_edges:
for _ in range(E):
    node1, node2, dist = map(int, input().split())
    adj_list[node1].append([node2, dist])
    adj_list[node2].append([node1, dist])

vertex1, vertex2 = map(int, input().split())


def dijkstra(start):

    pq = []
    distances = [INF] * (N + 1)

    # start node
    distances[start] = 0
    heapq.heappush(pq, (0, start))

    # repeat
    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)
        if distances[curr_vertex] < curr_dist:
            continue

        for next_vertex, w in adj_list[curr_vertex]:
            next_dist = curr_dist + w
            if distances[next_vertex] > next_dist:
                distances[next_vertex] = next_dist
                heapq.heappush(pq, (next_dist, next_vertex))

    return distances


dist_from_1_to = dijkstra(1)
dist_from_v1_to = dijkstra(vertex1)
dist_from_v2_to = dijkstra(vertex2)

v1_v2_path = dist_from_1_to[vertex1] + dist_from_v1_to[vertex2] + dist_from_v2_to[N]
v2_v1_path = dist_from_1_to[vertex2] + dist_from_v2_to[vertex1] + dist_from_v1_to[N]

ans = min(v1_v2_path, v2_v1_path)
if ans >= INF:
    print(-1)
else:
    print(ans)
