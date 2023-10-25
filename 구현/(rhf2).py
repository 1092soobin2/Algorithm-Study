# BOJ_20061_모노모노도미노2


# board [RED, BLUE, GREEN]
# block: . _ |

# RED에 블록 놓을 위치 선택
# 초록, 파랑으로 이동
# 경계 | 다른 블록 전까지 이동

# GREEN
# 행이 가득 차면 사라진다 & 1점 획득

# BLUE
# 열이 가득 차면 사라진다


# === input ===
BLOCK_LIST = [[], [[0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]]]
N = int(input())
block_info_list = [list(map(int, input().split())) for _ in range(N)]
LEN_EDGE = 10


# === algorithm ===
board = [[0] * LEN_EDGE for _ in range(LEN_EDGE)]
EMPTY, BLOCK = 0, 1


# 1. 블록 이동
def move_block(type_id, r, c):

    def check_boundary(block):
        for tr, tc in block:
            if 0 <= tr < LEN_EDGE and 0 <= tc < LEN_EDGE and board[tr][tc] == 0:
                continue
            else:
                return False
        return True

    loc_list = [[br + r, bc + c] for br, bc in BLOCK_LIST[type_id]]

    def move(dr, dc):
        global board
        curr_loc_list = loc_list
        next_loc_list = [[tr + dr, tc + dc] for tr, tc in curr_loc_list]
        while check_boundary(next_loc_list):
            curr_loc_list = next_loc_list
            next_loc_list = [[tr + dr, tc + dc] for tr, tc in curr_loc_list]
        for tr, tc in curr_loc_list:
            board[tr][tc] = BLOCK

    move(0, 1)
    move(1, 0)
    print_debug(f"1. move_block{type_id, r, c}")


# 2. 점수 획득
def get_score() -> int:
    global board
    num_line = 0

    # 1) Check GREEN area.
    for r in range(4, 10):
        if board[r][:4] == [BLOCK] * 4:
            num_line += 1
            board[r][:4] = [EMPTY] * 4

    # 2) Check BLUE area.
    for c in range(4, 10):
        if [board[r][c] for r in range(4)] == [BLOCK] * 4:
            num_line += 1
            for r in range(4):
                board[r][c] = EMPTY

    print_debug(f"2. get_score")
    return num_line


# 3. 연한 곳 체크
def check_empty_area():
    global board

    new_r = 9
    for r in range(9, 3, -1):
        if board[r][:4] != [EMPTY] * 4:
            board[new_r][:4] = board[r][:4]
            if r != new_r:
                board[r][:4] = [EMPTY] * 4
            new_r -= 1

    new_c = 9
    for c in range(9, 3, -1):
        if [board[r][c] for r in range(4)] == [EMPTY] * 4:
            for r in range(4):
                board[r][new_c] = board[r][c]
            if c != new_c:
                for r in range(4):
                    board[r][c] = EMPTY
            new_c -= 1

    if board[4][:4] != [EMPTY] * 4:
        for r in range(9, 5, -1):
            board[r][:4] = board[r - 2][:4]
        for r in range(5, 3, -1):
            board[r][:4] = [EMPTY]*4
    elif board[5][:4] != [EMPTY] * 4:
        for r in range(9, 5, -1):
            board[r][:4] = board[r - 1][:4]
        board[5][:4] = [EMPTY]*4

    if [board[r][4] for r in range(4)] != [EMPTY] * 4:
        for r in range(4):
            board[r][6:10] = board[r][4:8]
            board[r][4:6] = [EMPTY] * 2
    elif [board[r][5] for r in range(4)] != [EMPTY] * 4:
        for r in range(4):
            board[r][6:10] = board[r][5:9]
            board[r][5:6] = [EMPTY]

    print_debug(f"3. check_empty_area")


# 4. 한 판
def solution():

    score = 0
    for t, x, y in block_info_list:
        move_block(t, x, y)
        score += get_score()
        check_empty_area()

    total_block = 0
    for r in range(4):
        total_block += board[r][6:].count(BLOCK)
        total_block += board[r + 6][:4].count(BLOCK)

    return f"{score}\n{total_block}"


def print_debug(title=""):

    print("==============================")
    print(title)
    for r in range(LEN_EDGE):
        for c in range(LEN_EDGE):
            if r >= 4 and c >= 4:
                pass
            else:
                print(f"{board[r][c]:3}", end="")
        print()
    print("==============================")


# === output ===
print(solution())
