# (, 골4) Codetree_방화벽설치하기

# 64개
# 64*63*62/6 *64
# 4*(10^3) * 63*62/6
# 2*(10^3) * 2*7*31*2
# 124*(10^3) * 7 -> (10^6)

# === input ===
N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]
FIRE, WALL, EMPTY = 2, 1, 0


# === algorithm ===
def comb(arr, r):
    ret_list = []

    def dfs(start_i, acc):
        if len(acc) == r:
            ret_list.append(acc)
            return
        for i in range(start_i, len(arr)):
            dfs(i + 1, acc + [arr[i]])

    dfs(0, [])

    return ret_list


def simulate_all():

    def simulate_one(new_wall_list: list) -> int:

        ret_int = 0
        visited = [[False]*M for _ in range(N)]

        # 방화벽 설치
        board = [BOARD[r][:] for r in range(N)]
        for wr, wc in new_wall_list:
            if board[wr][wc] != EMPTY:
                return 0
            board[wr][wc] = WALL

        def spread():
            # bfs
            queue = [[r, c]]
            visited[r][c] = True

            while queue:
                curr_r, curr_c = queue.pop(0)
                for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] == EMPTY:
                        queue.append([nr, nc])
                        visited[nr][nc] = True
                        board[nr][nc] = FIRE

        # 불 퍼짐
        for r in range(N):
            for c in range(M):
                if board[r][c] == FIRE and not visited[r][c]:
                    spread()

        # 불 안 퍼진 공간 구하기
        for r in range(N):
            for c in range(M):
                if board[r][c] == EMPTY:
                    ret_int += 1

        print_debug(board)
        return ret_int

    max_empty = 0
    all_loc_list = [(r, c) for c in range(M) for r in range(N)]
    for three_loc_list in comb(all_loc_list, 3):
        max_empty = max(max_empty, simulate_one(three_loc_list))

    return max_empty


def print_debug(arr):
    if not debug:
        return

    print("===" * M)
    for r in range(N):
        for c in range(M):
            print(f"{arr[r][c]:3}", end="")
        print()
    print("===" * M)


# === output ===
debug = False
print(simulate_all())
