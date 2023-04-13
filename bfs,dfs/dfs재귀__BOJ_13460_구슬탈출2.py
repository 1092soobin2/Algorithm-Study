# dfs재귀__BOJ_13460_구슬탈출2
# 1. 재귀 dfs에서 continue vs. return 구분하기
# 2. 변수 업데이트 시에 원래 값 보존 여부 판단. ex) 자리가 안 바뀌었는데 바뀌었다고 생각하고 덮어써버림.
# 3. 예외 경우 하나만 찾고 홀라당 좋아하지 않기

'''
NxM 직사각형 보드
red     ->빼내기
blue    ->안 빼내기

- red 빠지면 성공
- blue 빠지면 실패
- 구슬이 더 이상 움직이지 않으면 동작을 멈춤.

ans: 최소 몇 번 만에 성공할 수 있는지
'''

import copy

direction_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# ===input===
N, M = map(int, input().split())
board = [input() for _ in range(N)]


def print_board(arr):
    print("========")
    for s in arr:
        print(s)
    print("========\n")


# ===algorithm===
def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < M


# 주어진 방향에서 가장 먼 빈 칸을 구하는 함수
def move_ball_from_to(arr, ball_loc: tuple, direction_id) -> tuple:

    # 도착지 구하기
    dr, dc = direction_list[direction_id]
    from_r, from_c = ball_loc
    to_r, to_c = from_r, from_c
    while check_boundary(to_r+dr, to_c+dc) and arr[to_r+dr][to_c+dc] == '.':
        to_r, to_c = to_r+dr, to_c+dc

    # 구슬 위치 업데이트
    # arr[to_r][to_c] = arr[from_r][from_c]       # 구슬 옮기기
    # arr[from_r][from_c] = '.'                   # 원래 구슬 자리는 빈 칸으로 만들기
    if from_r != to_r or from_c != to_c:
        # 다음 칸이 0이면 from_loc 반환
        if check_boundary(to_r+dr, to_c+dc) and arr[to_r+dr][to_c+dc] == '0':
            return from_r, from_c
        tmp_list = list(arr[to_r])
        tmp_list[to_c] = arr[from_r][from_c]
        arr[to_r] = ''.join(tmp_list)

        tmp_list = list(arr[from_r])
        tmp_list[from_c] = '.'
        arr[from_r] = ''.join(tmp_list)

    # 옮긴 위치 알려 주기
    return to_r, to_c


def check_hole_to_direction(tarr, ball_loc, direction_id) -> bool:
    dr, dc = direction_list[direction_id]
    from_r, from_c = ball_loc
    to_r, to_c = from_r, from_c
    while check_boundary(to_r + dr, to_c + dc) and tarr[to_r+dr][to_c+dc] != '#':
        to_r, to_c = to_r + dr, to_c + dc
        if tarr[to_r][to_c] == 'O':
            return True
    return False


def check_blue_to_direction(tarr, ball_loc, direction_id) -> bool:
    dr, dc = direction_list[direction_id]
    from_r, from_c = ball_loc
    to_r, to_c = from_r, from_c
    while check_boundary(to_r + dr, to_c + dc) and tarr[to_r+dr][to_c+dc] != '#':
        to_r, to_c = to_r + dr, to_c + dc
        if tarr[to_r][to_c] == 'B':
            return True
    return False


def dfs(arr, red_loc: tuple, blue_loc: tuple, history: list):
    global ans

    # 1) 멈추는 경우
    # TODO: 10번 초과이면 -1을 출력한다. -> ans = min(..) 해서 ans가 11이면 -1 출력하기
    if len(history) == 10:
        return

    for direction_id in range(4):
        check_red = check_hole_to_direction(arr, red_loc, direction_id)
        check_blue = check_hole_to_direction(arr, blue_loc, direction_id)
        # 1) 멈추는 경우
        if check_red and not check_blue:
            ans = min(ans, len(history) + 1)
            return
        elif check_blue:
            continue
        # 2) 계속하는 경우 (red, blue 둘 다 경로에 '0'이 없는 경우)
        else:
            # print(f"count {len(history)}, history {history}, direction: {direction_id}")
            # print_board(arr)
            # print()
            tmp_arr = copy.deepcopy(arr)
            next_red_loc = move_ball_from_to(tmp_arr, red_loc, direction_id)
            next_blue_loc = move_ball_from_to(tmp_arr, blue_loc, direction_id)
            # TODO: 구슬이 구슬에 막히는 경우도 있음 -> RBR 또는 BRB
            # if next_red_loc != move_ball_from_to(tmp_arr, next_red_loc, direction_id):
            if check_blue_to_direction(tmp_arr, next_red_loc, direction_id):
                next_red_loc = move_ball_from_to(tmp_arr, next_red_loc, direction_id)
            if next_red_loc == red_loc and next_blue_loc == blue_loc:
                continue
            dfs(tmp_arr, next_red_loc, next_blue_loc, history + [direction_id])


# ===output===
red_location, blue_location = (0, 0), (0, 0)
for tr in range(N):
    for tc in range(M):
        if board[tr][tc] == 'R':
            red_location = (tr, tc)
        elif board[tr][tc] == 'B':
            blue_location = (tr, tc)

ans = 11
dfs(board, red_location, blue_location, [])
print(ans if ans != 11 else -1)