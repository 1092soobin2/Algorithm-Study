# (2.5)__Codetree_술래잡기
# 


# 술래 정중앙

LOCATION = 0
DIRECTION = 1
DIRECTION_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]

CHASER = 0
RUNNER = 1
TREE = 2

# ===input===
n, m, h, num_of_turns = map(int, input().split())
runners = []            # [[(r, c), direction], ...
# [chaser(bool 0/1), runner(int), tree(bool 0/1)
board = [[[0]*3 for _ in range(n)] for _ in range(n)]


def get_inputs_and_make_board():
    global runners, board

    board[n//2][n//2][CHASER] = 1

    for _ in range(m):
        x, y, d = map(int, input().split())
        x, y = x-1, y-1
        runners.append([(x, y), d])
        board[x][y][RUNNER] += 1

    for _ in range(h):
        x, y = map(int, input().split())
        x, y = x-1, y-1
        board[x][y][TREE] = 1


# ===algorithm===

def run_and_chase(max_turn) -> int:

    def move_one_runner(runner) -> bool:
        (curr_r, curr_c), curr_d = runner

        # 지워진 runner
        if board[curr_r][curr_c][RUNNER] == 0:
            return False

        # 1) 다음 칸이 격자 O -> 방향 유지
        dr, dc = DIRECTION_LIST[curr_d]
        next_r, next_c = curr_r + dr, curr_c + dc
        # 2) 다음 칸이 격자 X -> 반대방향으로
        if not (0 <= next_r < n and 0 <= next_c < n):
            curr_d = (curr_d + 2) % 4
            runner[DIRECTION] = curr_d
            dr, dc = DIRECTION_LIST[curr_d]
            next_r, next_c = curr_r + dr, curr_c + dc
        # 3) 술래 X면 이동, 술래 O면 가만히. 나무 O여도 ㄱㅊ
        if board[next_r][next_c][CHASER] == 0:
            runner[LOCATION] = (next_r, next_c)
            board[curr_r][curr_c][RUNNER] -= 1
            board[next_r][next_c][RUNNER] += 1

        return True

    def move_chaser_from_to() -> (int, int):
        dr, dc = DIRECTION_LIST[chaser_d]
        nr, nc = chaser_r+dr, chaser_c+dc
        board[chaser_r][chaser_c][CHASER] = 0
        board[nr][nc][CHASER] = 1
        return nr, nc

    def see_and_pop_runners() -> int:
        num_of_runners = 0
        dr, dc = DIRECTION_LIST[chaser_d]
        nr, nc = chaser_r, chaser_c
        for _ in range(3):
            if not(0 <= nr < n and 0 <= nc < n):
                break
            # print(f"loc:{nr, nc}/runner:{board[nr][nc][RUNNER]}", end=" -> ")
            if board[nr][nc][TREE] == 0:
                num_of_runners += board[nr][nc][RUNNER]
                board[nr][nc][RUNNER] = 0
            nr, nc = nr+dr, nc+dc
        return num_of_runners

    chaser_r = chaser_c = n // 2
    turn = 1               # 움직일 때마다 +1
    point = 0

    # 달팽이 밖에서부터 counter_clockwise
    # 달팽이 안에서부터 clockwise
    while True:
        for d_change in [1, -1]:
            chaser_d = 0
            forward_count_list = list(range(1, n))
            if d_change == -1:
                chaser_d = 2
                forward_count_list = forward_count_list[::-1]
            for forward_count in forward_count_list:
                repeat = 2
                if forward_count == n-1:
                    repeat = 3

                for _ in range(repeat):
                    for cnt in range(forward_count):
                        # 1. 도망자 이동 (dist <= 3)
                        # run
                        for ri, runner in enumerate(runners):
                            if runner:
                                runner_r, runner_c = runner[LOCATION]
                                if abs(runner_r-chaser_r) + abs(runner_c-chaser_c) <= 3:
                                    if not move_one_runner(runner):
                                        runners[ri] = None

                        # 2. chase
                        # 1) 한 칸 이동
                        chaser_r, chaser_c = move_chaser_from_to()
                        if cnt == forward_count-1:
                            # 방향 바꿈
                            chaser_d = (chaser_d+d_change) % 4

                        # 2) 시야(3) 이내에 있는 도망자 (exception: 나무 칸 도망자)
                        num = see_and_pop_runners()
                        # 3) 점수 += tern * num_of_runner
                        point += turn*num

                        # 3. finish 1 turn
                        if turn == max_turn:
                            return point
                        turn += 1

def print_board():
    print("=========")
    for r in range(n):
        for c in range(n):
            print(board[r][c], end='')
        print()
    print("=========")


# ===output===
get_inputs_and_make_board()
ans = run_and_chase(num_of_turns)
print(ans)
