# (1.3, 골2) Codetree_2차원테트리스

# 파랑 보드에서 주어짐.

from functools import reduce

# === input ===
K = int(input())
block_list = [list(map(int, input().split())) for _ in range(K)]


# === algorithm ===
board = [[False] * 10 for _ in range(10)]
BLOCK_TYPE = [None, [[0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]]]   # . _ |


# 1. 파랑 보드에서부터 떨어짐
# block_info : [r, c, 블록 type]
def drop_block(block_info):

    # 경계 안 && 블락 없음 -> True
    def check_board(block: list) -> bool:
        # 경계 체크
        boundary_bool_list = map(lambda x: 0 <= x[0] < 10 and 0 <= x[1] < 10, block)
        boundary_bool = reduce(lambda x, y: x & y, boundary_bool_list)
        if not boundary_bool:
            return False
        # 블락 체크
        block_bool_list = map(lambda x: board[x[0]][x[1]], block)
        block_bool = reduce(lambda x, y: x | y, block_bool_list)
        return not block_bool

    def drop(direction):
        global board
        type_id, r, c = block_info
        dr, dc = direction
        block = list(map(lambda x: [x[0] + r, x[1] + c], BLOCK_TYPE[type_id]))

        while True:
            next_block = list(map(lambda x: [x[0] + dr, x[1] + dc], block))
            if not check_board(next_block):     # 경계 밖 || 블록 존재 -> break
                break
            block = next_block

        for r, c in block:
            board[r][c] = True

    drop([0, 1])            # drop to red
    drop([1, 0])            # drop to yellow
    print_debug(f"drop_block() done. type: {block_info[0]}, loc: {block_info[1:]}")


# 2. 점수 획득할 부분 블록 사라짐
# return : 획득 점수
def adjust_full_line() -> int:
    # red : red인지, yellow인지
    # idx : red면 콜럼 인덱스, yellow면 row 인덱스
    def check_full(red: bool, idx: int):
        if red:
            return reduce(lambda x, y: x & y, [board[r][idx] for r in range(4)])
        else:
            return reduce(lambda x, y: x & y, [board[idx][c] for c in range(4)])

    # return: 점수
    def adjust_red() -> int:
        global board
        ret_score = 0       # 점수
        curr_c = 9
        while curr_c > 5:
            # full line O -> 한 칸 씩 떙기기
            if check_full(True, curr_c):
                ret_score += 1
                for r in range(4):
                    board[r][5:curr_c + 1] = board[r][4:curr_c]

            # full line X -> 다음 col 살피기
            else:
                curr_c -= 1
        return ret_score

    # return: 점수
    def adjust_yellow() -> int:
        global board
        ret_score = 0
        curr_r = 9
        while curr_r > 5:
            # full line O -> 한 칸 씩 떙기기
            if check_full(False, curr_r):
                ret_score += 1
                for r in range(curr_r, 4, -1):
                    board[r][:4] = board[r - 1][:4]
            # full line X -> 다음 col 살피기
            else:
                curr_r -= 1
        return ret_score

    red_score = adjust_red()
    yellow_score = adjust_yellow()

    print_debug(f"adjust_full_line() done. score:{red_score + yellow_score}")

    return red_score + yellow_score


# 3. 연한 부분 블록 사라짐
def adjust_light_line():

    # red : red인지, yellow인지
    # idx : red면 콜럼 인덱스, yellow면 row 인덱스
    # return: idx 라인에 블록이 있으면 True 반환
    def check_exist(red: bool, idx: int) -> bool:
        if red:
            return reduce(lambda x, y: x | y, [board[r][idx] for r in range(4)])

        else:
            return reduce(lambda x, y: x | y, [board[idx][c] for c in range(4)])

    def adjust_red():
        global board
        if check_exist(True, 4):
            start = 4           # 움직이기 시작하는 콜럼 인덱스
        elif check_exist(True, 5):
            start = 5
        else:
            return
        for r in range(4):
            board[r][6:10] = board[r][start: start+4]
            board[r][4:6] = [False, False]

    def adjust_yellow():
        global board
        if check_exist(False, 4):
            diff = 2           # 이동할 로우 인덱스 차이
        elif check_exist(False, 5):
            diff = 1
        else:
            return
        for r in range(9, 5, -1):
            board[r][:4] = board[r - diff][:4]
        board[5][:4] = [False] * 4
        board[4][:4] = [False] * 4

    adjust_red()
    adjust_yellow()

    print_debug(f"adjust_light_line() done.")


# return:
#   - score
#   - red, yellow 보드의 블록 차지 칸의 개수 합
def solution() -> int:
    score = 0
    num_block = 0

    for block_info in block_list:
        drop_block(block_info)
        score += adjust_full_line()
        adjust_light_line()

    for r in range(4):
        for c in range(6, 10):
            if board[r][c]:
                num_block += 1
    for r in range(6, 10):
        for c in range(4):
            if board[r][c]:
                num_block += 1

    return f"{score}\n{num_block}"


def print_debug(title=""):
    if not DEBUG:
        return

    print("============================")
    print(title)
    for r in range(10):
        for c in range(10):
            if r > 3 and c > 3:
                continue
            if board[r][c]:
                print("0", end="")
            else:
                print("_", end="")
        print()
    print("============================")


# === output ===
DEBUG = False
# DEBUG = True
print(solution())
