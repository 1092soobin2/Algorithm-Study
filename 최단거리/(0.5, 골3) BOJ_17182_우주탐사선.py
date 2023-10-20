# (0.5, 골3) BOJ_17182_우주탐사선

# ana호
# 어떤 행성계를 탐사하기 위해 발사됨.
# 모든 행성을 탐사하는 데 걸리는 최소 시간
# 탐색할 행성의 개수
# 발사되는 행성의 위치
# 행성 간 이동 시간 (2차원 행렬)

from collections import deque
# import heapq


N, K = map(int, input().split())
adj_graph = [list(map(int, input().split())) for _ in range(N)]


def fw():
    global adj_graph

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if adj_graph[i][j] > adj_graph[i][k] + adj_graph[k][j]:
                    adj_graph[i][j] = adj_graph[i][k] + adj_graph[k][j]


answer = 1e9


def dfs(dist, curr, acc, ans):
    global answer

    if acc == N:
        answer = min(answer, ans)
        return

    if ans > answer:
        return

    for adj in range(N):
        if adj == curr or dist[adj] != -1:
            continue
        new_dist = dist[:]
        new_dist[adj] = dist[curr] + adj_graph[curr][adj]
        dfs(new_dist, adj, acc + 1, new_dist[adj])


def solution():
    fw()

    dist = [-1] * N
    dist[K] = 0
    dfs(dist, K, 1, 0)

    return answer


print(solution())
