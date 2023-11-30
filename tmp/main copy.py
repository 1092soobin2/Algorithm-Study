# (0.5, gol3) BOJ_15685_드래곤커브
# 22:10~


# 3가지 속성
# 1. 시작 점
# 2. 시작 방향
# 3. 세대

# 0세대: [(0, 0), (오른쪽), 길이 1]
# 1세대 = 0세대 (끔 점 기준 시계 방향 90도 회전) + 0세대 드래곤
# 2세대 = 1세대 (회전) + 1세대

# answer: 1*1 크기 정사각형 개수


# ===
N = int(input())
curve_start_list = [list(map(int, input().split())) for _ in range(N)]
curve_direction_list = [list() for _ in range(4)]        # list[세대] = [점 리스트]


# ===
def element_wise_diff(x, y):
    return [x[0] - y[0], x[1] - y[1]]


def element_wise_sum(x, y):
    return [x[0] + y[0], x[1] + y[1]]


def get_curve(direction, generation):
    global curve_direction_list

    direction_list = [[0, 1], [-1, 0], [-1, 0], [1, 0]]

    curve_list = curve_direction_list[direction]

    if curve_list and curve_list[generation]:
        return curve_list[generation]

    if not curve_list:
        curve_list = [list() for _ in range(11)]
        curve_list[0] = [[0, 0], direction_list[direction]]

    for i in range(generation + 1):
        if curve_list[i]:
            continue

        prev_curve = curve_list[i-1]
        last_point = prev_curve[-1]

        old_curve = [element_wise_diff(point, last_point) for point in prev_curve[::-1]]
        rotated = [[-c, r] for r, c in old_curve[1:]]
        new_curve = prev_curve[:] + [element_wise_sum(last_point, point) for point in rotated]

        curve_list[i] = new_curve

    curve_direction_list[direction] = curve_list
    return curve_list[generation]


def solution():

    grid = [[0] * 101 for _ in range(101)]

    for x, y, d, g in curve_start_list:
        curve = get_curve(d, g)
        print(d, g)
        print(curve_direction_list)

        for r, c in curve:
            gr, gc = x + c, y + -r
            if 0 <= gr <= 100 and 0 <= gc <= 100:
                grid[gr][gc] = 1

    answer = 0
    for r in range(100):
        for c in range(100):
            if sum([grid[r][c], grid[r+1][c], grid[r][c+1], grid[r+1][c+1]]) == 4:
                answer += 1

            if grid[r][c] == 1:
                print("0", end="")
            else:
                print("_", end="")
        print()
    return answer

# ===
print(solution())






