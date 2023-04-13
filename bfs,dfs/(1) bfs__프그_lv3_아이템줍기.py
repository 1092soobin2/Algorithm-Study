def solution(rectangle: list, characterX: int, characterY: int, itemX, itemY):
    answer = 0

    def print_arr_2d(arr, edge):
        def map_char(num):
            if num == 1:
                return "O"
            else:
                return "-"

        print("----------")
        for r in range(1, edge):
            # print(arr[:edge])
            print_list = list(map(map_char, arr[r][1:edge]))
            print(*print_list)
        print("----------\n")

    # 1. len(rectangle) == 1 -> abs(x1-x2) + ...
    # if len(rectangle) == 1:
    #     answer = abs(characterY - itemY) + abs(characterX - itemX)
    # 2. len(rec) == 2
    # else:
    EDGE = 102
    board = [[0] * EDGE  for _ in range(EDGE)]
    # 테두리 + 내부 1
    for rec in rectangle:
        left, down, right, up = map(lambda x: 2 * x, rec)
        for board_x in range(down, up+1):
            board[board_x][left:right+1] = [1]*(right+1-left)
    # 테두리 + 내부 0
    for rec in rectangle:
        left, down, right, up = map(lambda x: 2 * x, rec)
        # 직사각형 Toggle
        for board_x in range(down+1, up):
            board[board_x][left+1:right] = [0]*(right-left-1)
    # print_arr_2d(board, 25)

    characterX, characterY, itemX, itemY = map(lambda x: 2*x, [characterX, characterY, itemX, itemY])

    will_visited_stack = [(characterX, characterY, 0)]
    while will_visited_stack:
        curr_x, curr_y, ans = will_visited_stack.pop(0)
        if curr_x == itemX and curr_y == itemY:
            answer = ans//2
            break

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = curr_y+dy, curr_x+dx
            if  1 <= ny < EDGE and 1 <= nx < EDGE and board[ny][nx]:
                board[curr_y][curr_x] = False
                will_visited_stack.append((nx, ny, ans+1))
                    
    return answer