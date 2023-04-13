# BOJ_17142
from collections import deque

# ===input===
N, M = map(int, input().split())
ROOM = [list(map(int, input().split())) for _ in range(N)]

# ===algorithm===
WALL = 1


# 1. 조합 nCr
def combination(n: list, r: int) -> list:
    result = []

    def dfs(start:int, res: list):
        if len(res) == r:
            result.append(res[:])
            return

        for i in range(start, len(n)):
            res.append(n[i])
            dfs(i + 1, res)
            res.pop()

    dfs(0, [])
    return result


# 2. 몇 초 걸림 bfs
def count_second(virus: list) -> int:

    queue = deque([(start, 0) for start in virus])
    visited = [[False] * N for _ in range(N)]

    # 끝내야 하는지 확인하는 함수
    def check_virus() -> bool:
        for i in range(N):
            for j in range(N):
                if ROOM[i][j] == 0 and not visited[i][j]:
                    return False
        return True

    result = 0
    while queue:

        # if check_virus():
        #     return result

        (r, c), order = queue.popleft()
        # result = max(result, order)
        if ROOM[r][c] == 0:
            result = max(result, order)

        if not visited[r][c]:
            visited[r][c] = True

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if ROOM[nr][nc] != WALL and not visited[nr][nc]:
                    queue.append(((nr, nc), order + 1))
                    # 핫핫핫 이거 한 줄때문에 시간 초과
                    visited[nr][nc] = True

    if check_virus():
        return result
    else:
        return 1e9


# 4. algorithm
viruses_loc = []
for i in range(N):
    for j in range(N):
        if ROOM[i][j] == 2:
            viruses_loc.append((i, j))

ans = 1e9
for viruses in combination(viruses_loc, M):
    ans = min(ans, count_second(viruses))

# ===output===
print(ans if ans != 1e9 else -1)