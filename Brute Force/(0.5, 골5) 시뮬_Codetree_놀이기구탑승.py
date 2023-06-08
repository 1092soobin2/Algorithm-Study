# (0.5, 골5) Codetree_놀이기구탑승 15:05~

# n*n grid


import heapq

# === input ===
N = int(input())
like_list = [list(map(int, input().split())) for _ in range(N * N)]
EMPTY = 0
board = [[EMPTY]*N for _ in range(N)]


# === algorithm ===
def place_all():

    def place_one(student_number, like):
        global board

        # 배치할 위치 찾기
        loc_pq = []
        for r in range(N):
            for c in range(N):
                # 1. max(like) in 4 인접칸
                # 2. max(empty) in 4 adj
                # 3. min(r)
                # 4. min(c)
                if board[r][c] != EMPTY:
                    continue

                # check adj
                num_like, num_empty = 0, 0
                for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] == EMPTY:
                            num_empty += 1
                        elif board[nr][nc] in like:
                            num_like += 1
                # pq에 넣어주기
                loc_pq.append((-num_like, -num_empty, r, c))

        # pq 정렬
        heapq.heapify(loc_pq)

        # 배치하기
        r, c = loc_pq[0][2:]
        board[r][c] = student_number

    for info in like_list:
        place_one(info[0], info[1:])
        print_debug()


def get_score():
    ret_int = 0

    like_dict = dict([(info[0], info[1:]) for info in like_list])

    for r in range(N):
        for c in range(N):
            # like 개수 세기
            num_like = 0
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] in like_dict[board[r][c]]:
                        num_like += 1
            # 점수 계산
            ret_int += 10 ** (num_like - 1) if num_like != 0 else 0

    return ret_int


def print_debug():
    if debug:
        print(*like_list)
        for r in range(N):
            print(*board[r])


# === output ===
debug = False
place_all()
print(get_score())

# ans: 점수 총 합 (0/0 1/1 2/10 3/100 4/1000)


