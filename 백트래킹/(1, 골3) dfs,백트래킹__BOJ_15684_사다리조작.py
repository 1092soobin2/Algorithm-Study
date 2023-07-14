# (1, 골3) bruteforce__BOJ_15684_사다리조작

# H * N
# H : 세로선별 가로선 개수

# 가로선
# 연속하거나 접하면 안 됨

# === input ===
N, M, H = map(int, input().split())


# [1, 1] -> [1][1] - [1][2]
# [a, b] -> [a][b] - [a][b+1]
horizon_list = [list(map(int, input().split())) for _ in range(M)]


# === algorithm ===
# [가로idx][세로idx] = (연결선 idx) (0이면 연결 X)
# 0번 row, 0 col -> dummy
link_arr = [[0] * (N + 1) for _ in range(H + 1)]
down_arr = [[0] * (N + 1) for _ in range(H + 1)]


def init():
    global link_arr

    link_arr[0] = [1] * (N + 1)     # 첫 줄은 N/A

    for a, b in horizon_list:
        link_arr[a][b] = b + 1
        link_arr[a][b + 1] = b

    for c in range(N, 0, -1):
        down_r = H
        for r in range(H, 0, -1):
            if link_arr[r][c] == 0:
                down_arr[r][c] = down_r
            else:
                down_r = r


# 사다리 타기 O(N*H) 10 * 300 = 3000
# return : 도착 column 번호
def go_ladder(column) -> int:
    for r in range(1, H + 1):
        column = link_arr[r][column] if link_arr[r][column] != 0 else column   # 가로선 있으면 갱신
    return column


def check_all_ladder():
    for column in range(1, N + 1):
        if not go_ladder(column) == column:
            return False
    return True


# 모든 경우 O(N*H) 10 * 300 = 3000
def dfs(acc, ans):
    global link_arr

    if acc >= ans:
        return ans

    if check_all_ladder():
        return acc
    
    if acc == 3:
        return -1
    
    min_res = 4
    for r in range(1, H + 1):
        for c in range(1, N):
            # 위 연결이 있는 연결의 경우
            if (link_arr[r][c] == 0 and link_arr[r][c + 1] == 0) and not (link_arr[r - 1][c] == 0 and link_arr[r - 1][c + 1] == 0):
                link_arr[r][c], link_arr[r][c+1] = c+1, c
                res = dfs(acc + 1, min_res)
                link_arr[r][c], link_arr[r][c + 1] = 0, 0
                
                if res == acc + 1:
                    return res
                elif res != -1:
                    min_res = min(res, min_res)

    return min_res if min_res != 4 else -1


def solution():

    init()
    print(dfs(0, 4))


# === output ===

# ans: i 세로선의 결과가 i가 되도록 하는 min(가로선 개수)
# 불가능 or >3 -> -1
solution()
