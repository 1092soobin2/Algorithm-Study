# (1, 골4) Codetree_드래곤커브


# dragon curve
# 0 -> 길이가 1인 선분
# 1 -> 0차 + rotated 0차
# ...
# n -> n-1차 + rotated n-1차

# 100 * 100 board
    # 각 칸의 "점"을 의미한다: [0][0] ~ [100][100]

# n개의 dragon_curve

DIRECTION_LIST = [[0, 1], [-1, 0], [0, -1], [1, 0]]
# === input ===
N = int(input())
# dragon_curve -> dc
dc_list = [list(map(int, input().split())) for _ in range(N)] # [시작 r, 시작 c, d, g]
dc_road = []*4
# dc_board = [[[False, False] for _ in range(101)] for _ in range(101)]   # 아래로 |, 오른쪽으로 _
dc_board = [[False]*101 for _ in range(101)]


# === algorithm ===
# 1. 방향 별로 다음 위치를 저장한다.
def init_dc_road():
    global dc_road

    # 첫 선분
    dc_road = [[[[0, 0], DIRECTION_LIST[i]]] for i in range(4)]

    # 10차까지 가능
    for direction_id in range(4):
        ith_dc_road = dc_road[direction_id]
        for _ in range(11):
            # n-1 curve를 시계 방향으로 90도 회전한 커브
            last_curve = ith_dc_road[-1]    # n-1 curve
            new_curve = last_curve[:]       # n curve
            r, c = last_curve[-1]           # n-1 커브의 끝점
            for r2, c2 in last_curve[::-1][1:]:
                dr, dc = r2 - r, c2 - c     # r2 = r + dr = r + (r2 - r)
                new_curve.append([r + dc, c - dr])
            ith_dc_road.append(new_curve)
            if debug:
                print(new_curve)
        if debug:
            print()


# 2. 드래곤 커브를 그린다.
def draw_dc_board():
    global dc_board

    for r, c, d, g in dc_list:
        # curr_r, curr_c = r, c
        for dr, dc in dc_road[d][g]:
            nr, nc = r + dr, c + dc
            # if curr_r == nr:
            #     dc_board[curr_r][min(curr_c, nc)][1] = True
            # else:
            #     dc_board[min(curr_r, nr)][curr_c][0] = True
            # curr_r, curr_c = nr, nc
            dc_board[nr][nc] = True


# 3. count square
def count_square():
    ret_int = 0

    for r in range(100):
        for c in range(100):
            # if dc_board[r][c][0] and dc_board[r][c][1] and dc_board[r][c + 1][0] and dc_board[r + 1][c][1]:
            #     ret_int += 1
            if dc_board[r][c] and dc_board[r][c + 1] and dc_board[r + 1][c] and dc_board[r + 1][c + 1]:
                ret_int += 1
    return ret_int


def print_dc_board(edge=101):
    for r in range(edge):
        for c in range(edge):
            if dc_board[r][c] == [True, True]:
                print("+", end="")
            elif dc_board[r][c][0]:
                print("|", end="")
            elif dc_board[r][c][1]:
                print("_", end="")
            else:
                print("0", end="")
        print()


# === output ===
debug = False
init_dc_road()
draw_dc_board()
# ans: 단위 정사각형의 개수
print(count_square())
