# (1, 골2) bfs_Codetree_색깔폭탄
import heapq

# n * n

# === input ===
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
EMPTY, BLACK, RED = -2, -1, 0


# === algorithm ===

# 1. max(폭탄 묶음) 제거됨
        # 2개 이상의 폭탄
        # 모두 같은 색깔이거나, 빨간색을 포함
        # 빨간색만으로 이루어지면 안 됨!
    # 2. min(red)
    # 3. max(r)   *기준점: not RED, max(r), min(c)
    # 4. min(c)
def remove_bomb() -> int:
    global board

    def find_bomb():
        # (폭탄 개수, 빨간 색 개수, -r, c)
        bomb_pq = []

        visited = [[False]*N for _ in range(N)]

        def bfs(start):

            # 2개
            queue = [start]
            visited[start[0]][start[1]] = True
            color = board[start[0]][start[1]]

            bomb_list = [start]

            while queue:
                curr_r, curr_c = queue.pop(0)

                for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if board[nr][nc] == RED or board[nr][nc] == color:
                            queue.append([nr, nc])
                            visited[nr][nc] = True
                            bomb_list.append((nr, nc))

            # TODO: RED 표시 복구, pq에 넣어주기
            num_red = 0
            for tr, tc in bomb_list:
                if board[tr][tc] == RED:
                    visited[tr][tc] = False
                    num_red += 1

            if len(bomb_list) >= 2:
                bomb_pq.append((-len(bomb_list), num_red, -start[0], start[1], bomb_list))

        # red -> 깍두기, red부터 시작 불가능
        for r in range(N - 1, -1, -1):
            for c in range(N):
                if not visited[r][c] and board[r][c] > 0:
                    bfs([r, c])
        heapq.heapify(bomb_pq)

        if bomb_pq:
            return bomb_pq[0][4]
        else:
            return []

    removed = find_bomb()
    for br, bc in removed:
        board[br][bc] = EMPTY

    print_debug("remove")

    return len(removed) ** 2


# 2. 중력 작용
def gravity():
    global board

    for c in range(N):
        floor = N - 1
        for r in range(N - 1, -1, -1):
            # BLACK은 안 움직임
            if board[r][c] == BLACK:
                floor = r - 1
            # 폭탄은 떨어진다
            elif board[r][c] != EMPTY:
                if floor == r:
                    floor -= 1
                else:
                    board[floor][c] = board[r][c]
                    board[r][c] = EMPTY
                    floor -= 1

    print_debug("gravity")


# 3. 반시계 회전
def rotate():
    global board
    new_board = [[-2]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_board[(N - 1) - c][r] = board[r][c]
    board = new_board
    print_debug("rotate")


# 4. 중력 작용

# 5. 점수: 제거된 돌


def print_debug(title=""):
    if debug:
        print("=======================")
        print(title)
        for r in range(N):
            print(*board[r])
        print("=======================")


# === output ===
debug = False
# ans: 최종 점수
ans = 0

while True:
    score = remove_bomb()
    if score == 0:
        break
    ans += score
    gravity()
    rotate()
    gravity()

print(ans)
