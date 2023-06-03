# (1, 골2) Codetree_2차원테트리스


# type
# 1 .
# 2 _
# 3 |

# 파란색 보드: [위치, 타일 종류]
# 빨 & 노 쪽으로 미뤄짐

# === input ===
K = int(input())
command_list = [list(map(int, input().split())) for _ in range(K)]

board = [[False]* 10 for _ in range(10)]
EMPTY = 0


# === algorithm ===
def drop(comm):

    def drop_block(r, c, block_type):
        global board
        block_list = [[(0, 0)], [(0, 0), (0, 1)], [(0, 0), (1, 0)]]

        for dr, dc in block_list[block_type - 1]:
            br, bc = r + dr, c + dc
            board[br][bc] = True

    def drop_to_red(block_type, loc_r, loc_c):

        if block_type == 1:
            for c in range(5, 10):
                if c == 9 or board[loc_r][c + 1]:
                    drop_block(loc_r, c, 1)
                    break
        elif block_type == 2:
            for c in range(4, 9):
                if c == 8 or board[loc_r][c + 2]:
                    drop_block(loc_r, c, 2)
                    break
        elif block_type == 3:
            for c in range(5, 10):
                if c == 9 or board[loc_r][c + 1] or board[loc_r + 1][c + 1]:
                    drop_block(loc_r, c, 3)
                    break

    def drop_to_yellow(block_type, loc_r, loc_c):

        if block_type == 1:
            for r in range(5, 10):
                if r == 9 or board[r + 1][loc_c]:
                    drop_block(r, loc_c, 1)
                    break
        elif block_type == 2:
            for r in range(5, 10):
                if r == 9 or (board[r + 1][loc_c] or board[r + 1][loc_c + 1]):
                    drop_block(r, loc_c, 2)
                    break
        elif block_type == 3:

            for r in range(4, 9):
                if r == 8 or board[r + 2][loc_c]:

                    if debug and [block_type, loc_r, loc_c] == [3, 2, 2]:
                        print_debug("sdasfdsgffdhjgk\nbefore yellow drop")
                    drop_block(r, loc_c, 3)
                    if debug and [block_type, loc_r, loc_c] == [3, 2, 2]:
                        print_debug("sdasfdsgffdhjgk\nafter yellow drop")

                    break

    drop_to_red(*comm)
    drop_to_yellow(*comm)

    if debug:
        print(*comm)
        print_debug()


def disappear() -> int:
    global board

    ret_int = 0

    def move_red(start_c, next_c, diff_c):
        for r in range(4):
            board[r][next_c:next_c + diff_c] = board[r][start_c:start_c + diff_c]
            board[r][start_c:next_c] = [False]*(next_c - start_c)
        # for r in range(4):
        #     board[r][start_c:] = [False] * (6 - start_c) + board[r][start_c:start_c + 4]

    def move_yellow(diff_r):
        for r in range(9, 5, -1):
            board[r][:4] = board[r - diff_r][:4]

        board[4][:4] = [False]*4
        board[5][:4] = [False]*4

    # 꽉찬 부분 삭제하기
    c = 9
    while True:
        now_col = [board[r][c] for r in range(4)]
        if sum(now_col) == 4:
            ret_int += 1
            move_red(4, 5, c - 4)
        elif sum(now_col) == 0:
            break
        else:
            c -= 1

    r = 9
    while True:
        now_row = board[r][:4]
        if sum(now_row) == 4:
            ret_int += 1
            board[5:r + 1] = board[4:r]
        elif sum(now_row) == 0:
            break
        else:
            r -= 1

    # 연한 부분 밀기
    semi_red = list(zip(*board[:4]))
    if sum(semi_red[4]) != 0:
        move_red(4, 6, 4)
    elif sum(semi_red[5]) != 0:
        move_red(5, 6, 4)

    if sum(board[4][:4]) != 0:
        move_yellow(2)
    elif sum(board[5][:4]) != 0:
        move_yellow(1)



    if debug:
        print_debug()

    return ret_int


def print_debug(title=""):
    print("================")
    print(title)
    for r in range(10):
        for c in range(10):
            if r > 3 and c > 3:
                continue
            elif board[r][c]:
                print("0", end="")
            else:
                print("_", end="")
        print()
    print("================")


def get_block_num():
    ret_int = 0

    for r in range(4):
        ret_int += sum(board[r][6:])

    for r in range(6, 10):
        ret_int += sum(board[r][:4])

    return ret_int


# === output ===
debug = True
answer = 0
for command in command_list:
    drop(command)
    answer += disappear()


print(answer)
print(get_block_num())
