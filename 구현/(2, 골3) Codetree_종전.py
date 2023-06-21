# (2, 골3) Codetree_종전

# 1~100 숫자
# n*n grid

# === input ===
N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
ROW, COL = 0, 1


# === algorithm ===
# ret: 가능한 사각형 리스트
def get_tilted_rectangles() -> list:

    ret_list = []
    direction_list = [[0, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]

    def dfs(point_list):
        # 3개의 점이 정해지면 나머지 1개도 정해짐
        if len(point_list) == 3:
            p0, p1, p2 = point_list
            p3 = [p2[ROW] - (p1[ROW] - p0[ROW]), p2[COL] - (p1[COL] - p0[COL])]
            point_list.append(p3)
            ret_list.append(point_list)
            return

        dr, dc = direction_list[len(point_list)]        # 점 개수에 따라 방향을 정할 수 있다.
        nr, nc = point_list[-1][ROW] + dr, point_list[-1][COL] + dc
        while 0 <= nr < N and 0 <= nc < N:
            # 2번쨰 점이면 -> () <= point_list[0][ROW]
            if len(point_list) == 2:
                if (point_list[-1][COL] - nc) > point_list[0][COL]:
                    break

            dfs(point_list + [[nr, nc]])
            nr, nc = nr + dr, nc + dc

    for r in range(2, N):
        for c in range(1, N - 1):
            dfs([[r, c]])

    return ret_list


# ret: 사각형이 주어졌을 때 인구 차이
def count_popularity(rectangle) -> int:
    # 2   3
    #   1
    # 4   5
    # 3 : 오 O, 위 X
    # 2 : 위 O, 왼 X
    # 4 : 왼 O, 아 X
    # 5 : 아 O, 오 X
    popularity = [0] * 6

    def get_tribute_num():
        tribute_num = 0
        if r < rectangle[2][ROW]:  # 2 | 3
            if c <= rectangle[2][COL]:
                tribute_num = 2
            else:
                tribute_num = 3
        elif r > rectangle[0][ROW]:  # 4 | 5
            if c < rectangle[0][COL]:
                tribute_num = 4
            else:
                tribute_num = 5
        elif c < rectangle[3][COL]:  # 2 | 4
            if r < rectangle[3][ROW]:
                tribute_num = 2
            else:
                tribute_num = 4
        elif c > rectangle[1][COL]:  # 3 | 5
            if r <= rectangle[1][ROW]:
                tribute_num = 3
            else:
                tribute_num = 5
        else:  # 1 | 2 | 3 | 4 | 5
            if r < rectangle[3][ROW] and c < rectangle[2][COL] and r < rectangle[3][ROW] - (c - rectangle[3][COL]):
                tribute_num = 2
            elif r < rectangle[1][ROW] and c > rectangle[2][COL] and r < rectangle[2][ROW] + (c - rectangle[2][COL]):
                tribute_num = 3
            elif r > rectangle[3][ROW] and c < rectangle[0][COL] and r > rectangle[3][ROW] + (c - rectangle[3][COL]):
                tribute_num = 4
            elif r > rectangle[1][ROW] and c > rectangle[0][COL] and r > rectangle[0][ROW] - (c - rectangle[0][COL]):
                tribute_num = 5
            else:
                tribute_num = 1
        return tribute_num

    if DEBUG:
        print("\n====================================")
        print(rectangle)
    for r in range(N):
        for c in range(N):
            t_num = get_tribute_num()
            if DEBUG:
                char = str(t_num)
                if t_num == 1:
                    char = "_" + str(t_num) + "_"
                print(f"{char:4}", end="")
            popularity[t_num] += BOARD[r][c]
        if DEBUG:
            print()
    if DEBUG:
        print(popularity[1:])
        print("====================================")

    return max(popularity[1:]) - min(popularity[1:])


def solution():
    ret_int = 1e9
    for rectangle in get_tilted_rectangles():
        ret_int = min(ret_int, count_popularity(rectangle))
    return ret_int


# === output ===
DEBUG = False
# DEBUG = True

# min(max(인구) - min(인구)) 을 출력하시오.
print(solution())
