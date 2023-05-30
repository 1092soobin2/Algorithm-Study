# (1, 골3) 시뮬__Codetree_생명과학부랩인턴

# n*m board

# 곰팡이 [height, direction, speed]




# === input ===
N, M, K = map(int, input().split())
board = [[list() for _ in range(M)] for _ in range(N)]
SPEED, DIRECTION, HEIGHT = 0, 1, 2
DIRECTION_LIST = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def init_board():
    global board

    for _ in range(K):
        info = list(map(int, input().split()))
        if info[3] == 1:
            info[3] = 0
        elif info[3] == 2:
            info[3] = 2
        elif info[3] == 3:
            info[3] = 1
        elif info[3] == 4:
            info[3] = 3
        board[info[0] - 1][info[1] - 1].append(info[2:])

    if debug:
        print_debug()


# === algorithm ===
index_col = 0


# 1. 열 탐색: 제일 위의 곰팡이 채취 -> 그 칸은 빈 칸이 됨
def collect():
    global board

    for r in range(N):
        if board[r][index_col]:
            ret_height = board[r][index_col][0][HEIGHT]
            board[r][index_col].clear()
            return ret_height

    if debug:
        print_debug("채취 이후")
    return 0


# 2. 곰팡이 이동
# 3. 한 칸에 곰팡이가 두 마리 이상일 떄는, 크기가 큰 곰팡이만 남는다.
def move_all_mold():
    global board

    def move_one_mold(start_r, start_c) -> (int, int):
        speed, direction = board[start_r][start_c][0][SPEED], board[start_r][start_c][0][DIRECTION]

        direction = [direction]

        def move_one_elem(elem, forward, d, max_elem) -> int:
            while forward > 0:
                # max elem쪽으로 이동
                if d == 1:
                    can_go = max_elem - elem
                    if can_go >= forward:
                        elem += forward
                        forward = 0
                    else:
                        forward -= can_go
                        elem = max_elem
                        d = -1
                        direction[0] = (direction[0] + 2) % 4
                # 0쪽으로 이동
                else:
                    can_go = elem - 0
                    if can_go >= forward:
                        elem -= forward
                        forward = 0
                    else:
                        forward -= can_go
                        elem = 0
                        d = 1
                        direction[0] = (direction[0] + 2) % 4
            return elem

        dr, dc = DIRECTION_LIST[direction[0]]
        if dr != 0:
            next_r, next_c = move_one_elem(start_r, speed % (2 * (N - 1)), dr, N - 1), start_c,
        else:
            next_r, next_c = start_r, move_one_elem(start_c, speed % (2 * (M - 1)), dc, M - 1)

        return next_r, next_c, direction[0]

    new_board = [[list() for _ in range(M)] for _ in range(N)]
    #     1) d, s에 따라 이동
    #     2) 벽에 도달하면 ,d를 반대로 바꾸고 이동
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                nr, nc, nd = move_one_mold(r, c)
                board[r][c][0][DIRECTION] = nd
                new_board[nr][nc].append(board[r][c][0])

    for r in range(N):
        for c in range(M):
            if len(new_board[r][c]) > 1:
                # 크기가 가장 큰 곰팡이
                biggest_mold = new_board[r][c][0]
                for mold in new_board[r][c]:
                    if biggest_mold[HEIGHT] < mold[HEIGHT]:
                        biggest_mold = mold
                new_board[r][c] = [biggest_mold]

    board = new_board

    if debug:
        print_debug("곰팡이 이동")


# 4. 다음 열로 이동
def move_col():
    global index_col
    index_col += 1


def print_debug(title=""):
    print("====================")
    print(title)
    print("           |"*index_col, index_col)
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                print(f"{board[r][c]}|", end="")
            else:
                print("           |", end="")
        print()
    print("====================")


# === output ===
debug = False

init_board()

ans = 0
for _ in range(M):
    ans += collect()
    move_all_mold()
    move_col()

print(ans)


# ans: sum of height
