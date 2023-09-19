
N = int(input())
M = int(input())
dist_graph = [[1e9] * N for _ in range(N)]


for _ in range(M):
    a, b, c = map(int, input().split())
    dist_graph[a - 1][b - 1] = min(dist_graph[a - 1][b - 1], c)


for i in range(N):
    dist_graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist_graph[i][j] > dist_graph[i][k] + dist_graph[k][j]:
                dist_graph[i][j] = dist_graph[i][k] + dist_graph[k][j]


for r in range(N):
    for c in range(N):
        print(dist_graph[r][c] if dist_graph[r][c] != 1e9 else 0, end=" ")
    print()
