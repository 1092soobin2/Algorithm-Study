import heapq


def solution(num_of_nodes, s, a, b, fares):
    answer = 0

    adj_list = [list() for _ in range(num_of_nodes + 1)]
    for v1, v2, cost in fares:
        adj_list[v1].append((v2, cost))
        adj_list[v2].append((v1, cost))

    def dijkstra(start_v) -> list:

        INF = int(1e9)
        # 2
        pq = []
        distances = [INF] * (num_of_nodes + 1)

        distances[start_v] = 0
        heapq.heappush(pq, (0, start_v))

        while pq:
            curr_dist, curr_v = heapq.heappop(pq)

            if curr_dist > distances[curr_v]:
                continue

            for next_v, w in adj_list[curr_v]:
                next_dist = curr_dist + w
                if distances[next_v] > next_dist:
                    distances[next_v] = next_dist
                    heapq.heappush(pq, (next_dist, next_v))

        return distances

    dist_list = [[]]
    for v in range(1, num_of_nodes + 1):
        dist_list.append(dijkstra(v))

    answer = dist_list[s][a] + dist_list[s][b]
    for v in range(1, num_of_nodes + 1):
        new_answer = dist_list[s][v] + dist_list[v][a] + dist_list[v][b]
        if answer > new_answer:
            answer = new_answer

    return answer