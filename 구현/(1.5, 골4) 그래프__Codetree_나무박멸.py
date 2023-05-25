# (1.5, 골4) 그래프__Codetree_나무박멸

# === input ===
N, M, K, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
EMPTY, WALL = 0, -1
injected = [[0]*N for _ in range(N)]        # 제초제 유무


# 1. (동시) 인접칸 나무 개수만큼 성장 (0-4)
def grow():
    global grid

    for r in range(N):
        for c in range(N):
            # TODO: 제초제가 있으면 당연히 0이라고 가정
            if grid[r][c] > 0:
                for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
                        grid[r][c] += 1

    if debug:
        print_debug()


# 2. (동시) 기존 나무들은 (벽 X && 나무 X && 제초제 X)인 인접칸에 번식
def propagate():
    global grid

    new_grid = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:
                # 기존 나무
                new_grid[r][c] = grid[r][c]
                # 번식
                adj_loc = []
                for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == EMPTY and injected[nr][nc] == 0:
                        adj_loc.append([nr, nc])
                if adj_loc:
                    for nr, nc in adj_loc:
                        new_grid[nr][nc] += grid[r][c] // len(adj_loc)
            # 벽 복사
            elif grid[r][c] == WALL:
                new_grid[r][c] = WALL

    grid = new_grid

    if debug:
        print_debug()


# 3. 가장 많은 칸에 제초제 뿌린다. (min r -> min c)
def inject() -> int:
    global injected, grid

    def spread(r, c, inject_flag=False) -> int:
        ret_removed = grid[r][c]

        if inject_flag:
            grid[r][c] = 0
            injected[r][c] = C

        for dr, dc in [[-1, -1], [1, -1], [-1, 1], [1, 1]]:
            tr, tc = r, c
            for _ in range(K):
                tr, tc = tr + dr, tc + dc
                if 0 <= tr < N and 0 <= tc < N:

                    if grid[tr][tc] <= 0:
                        if inject_flag:
                            injected[tr][tc] = C
                        break
                    else:
                        if inject_flag:
                            grid[tr][tc] = 0
                            injected[tr][tc] = C
                        ret_removed += grid[tr][tc]

        return ret_removed

    # 1년 지남
    for r in range(N):
        for c in range(N):
            if injected[r][c] > 0:
                injected[r][c] -= 1

    # 제초제 뿌릴 위치 선정
    inject_loc = [0, 0]
    max_removed = 0
    for r in range(N):
        for c in range(N):
            # 대각선으로 퍼짐
            if grid[r][c] > 0:
                removed = spread(r, c)
                if max_removed < removed:
                    max_removed = removed
                    inject_loc = [r, c]

    # 제초제 뿌리기
    spread(*inject_loc, inject_flag=True)

    if debug:
        print_debug(f"inject_loc{inject_loc}")
    return max_removed


def print_debug(title=""):
    print(title)
    for r in range(N):
        for c in range(N):
            print(f"{grid[r][c]:4}", end="")
        print("\t\t", end="")
        for c in range(N):
            print(f"{injected[r][c]:4}", end="")
        print()
    print()


# === output ===
# ans: M년 동안 박멸한 나무 그루 수
debug = False
answer = 0
for _ in range(M):
    grow()
    propagate()
    answer += inject()
print(answer)
