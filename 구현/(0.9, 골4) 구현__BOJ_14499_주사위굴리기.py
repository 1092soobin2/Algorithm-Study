# 21:34~ 22:02 22:10

# (0.5, 골4) BOJ_14499_주사위굴리기

# N*M grid
# 오른쪽 = 동쪽, 위쪽 북쪽

# dice
# 지도 위에 윗 면이 1이고
# 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며
# 놓여져 있는 곳의 좌표는 (x, y) 이다
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.



# answer: 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램


# === input ===
N, M, R, C, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
move_list = list(map(int, input().split()))
ROLL_LIST = [[0, 0],
             [3, 1, 0, 5, 4, 2],
             [2, 1, 5, 0, 4, 3],
             [4, 0, 2, 3, 5, 1],
             [1, 5, 2, 3, 0, 4]]
DIRECTION_LIST = [[0, 0],
                  [0, 1],
                  [0, -1],
                  [-1, 0],
                  [1, 0]]


# === algorithm ===
#       1 2 3 4 5 6
# (동)   4 2 1 6 5 3
# (서)   3 2 6 1 5 4
# (남)   2 6 3 4 1 5
# (북)   5 1 3 4 6 2


dice = [0] * 6
dice_info = list(range(6))


def get_up_side():
    return dice[dice_info[0]]


def get_bottom_side():
    return dice[dice_info[5]]


def roll_dice(direction):
    global dice_info
    dice_info = [dice_info[i] for i in ROLL_LIST[direction]]
    # print(dice_info)


def move_dice(direction):
    global R, C, grid, dice

    dr, dc = DIRECTION_LIST[direction]
    nr, nc = R + dr, C + dc

    # 주사위는 지도의 바깥으로 이동시킬 수 없다.
    # 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
    if not (0 <= nr < N and 0 <= nc < M):
        return False

    R, C = nr, nc
    roll_dice(direction)
    # 0이면 -> 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
    if grid[R][C] == 0:
        grid[R][C] = get_bottom_side()
    # 0이 아닌 경우 -> 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    else:
        dice[dice_info[5]] = grid[R][C]
        grid[R][C] = 0
    # print(f"direction: {DIRECTION_LIST[direction]}, dice: {R, C} {[dice[i] for i in dice_info]}, grid:{grid}")
    return True


def solution():

    for direction in move_list:
        if move_dice(direction):
            print(get_up_side())


# === output ===
solution()
