# (0.5, 골4) Codetree_격자숫자놀이

from collections import defaultdict

# === input ===
target_r, target_c, target_num = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]


# === algorithm ===
def operate():
    global board

    len_row, len_col = len(board), len(board[0])

    def operate_by_row():
        global board

        max_col = 0
        item_list = []
        for r in range(len_row):
            # COUNT {숫자:빈도수}
            cnt_dict = defaultdict(int)
            for c in range(len_col):
                if board[r][c] == 0:
                    continue
                cnt_dict[board[r][c]] += 1

            # (숫자, 빈도수) ORDER BY 빈도수 ASC, 숫자 ASC
            item_list.append(list(cnt_dict.items()))
            item_list[-1].sort(key=lambda x: (x[1], x[0]))
            max_col = max(max_col, 2 * len(item_list[-1]))

        # 숫자 입력
        new_board = [[0] * max_col for _ in range(len_row)]
        for r in range(len_row):
            for i in range(len(item_list[r])):
                new_board[r][2*i:2*i + 2] = item_list[r][i]
        board = new_board

        print_debug()

    def operate_by_col():
        global board

        max_row = 0
        item_list = []
        for c in range(len_col):
            # COUNT {숫자:빈도수}
            cnt_dict = defaultdict(int)
            for r in range(len_row):
                if board[r][c] == 0:
                    continue
                cnt_dict[board[r][c]] += 1

            # (숫자, 빈도수) ORDER BY 빈도수 ASC, 숫자 ASC
            item_list.append(list(cnt_dict.items()))
            item_list[-1].sort(key=lambda x: (x[1], x[0]))
            max_row = max(max_row, 2 * len(item_list[-1]))

        new_board = [[0] * len_col for _ in range(max_row)]
        for c in range(len_col):
            for i in range(len(item_list[c])):
                new_board[2*i][c] = item_list[c][i][0]
                new_board[2*i + 1][c] = item_list[c][i][1]
        board = new_board

        print_debug()

    # 1. #(행) >= #(열) -> 모든 행에 대하여 정렬, (숫자, 출현 빈도) 출력
    if len_row >= len_col:
        operate_by_row()
    # 2. #(행) <  #(열) -> 모든 열에 대하여 정렬
    else:
        operate_by_col()

    # 3. #(행) > 100 || #(열) > 100  100 초과하면 뒤에서 버림.

    if len(board) > 100:
        board = board[:100]
    if len(board[0]) > 100:
        board = [board[r][:100] for r in range(len(board))]



def print_debug(title=""):
    if not DEBUG:
        return

    print("=====================")
    print(title)
    for r in range(len(board)):
        for c in range(len(board[0])):
            print(f"{board[r][c]:3}", end="")
        print()
    print("=====================\n")


# === output ===
DEBUG = False

time = 0
while time <= 100:
    if target_r <= len(board) and target_c <= len(board[0]) and board[target_r-1][target_c-1] == target_num:
        break
    time += 1
    operate()



if time > 100:
    print(-1)
else:
    print(time)

