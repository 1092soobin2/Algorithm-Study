from functools import reduce


WALL = 1
LEN_BOARD = 0


def check_boundary(robot_loc):
    [r1, c1], [r2, c2] = robot_loc
    return 0 <= r1 < LEN_BOARD and 0 <= c1 < LEN_BOARD and 0 <= r2 < LEN_BOARD and 0 <= c2 < LEN_BOARD


def check_not_wall(arr, robot_loc):
    [r1, c1], [r2, c2] = robot_loc
    return arr[r1][c1] != WALL and arr[r2][c2] != WALL

# 이동
def get_moved_list(arr, robot_loc) -> list:
    
    ret_list = []
    
    [r1, c1], [r2, c2] = robot_loc
    for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        next_robot_loc = [[r1+dr, c1+dc], [r2+dr, c2+dc]]
        if check_boundary(next_robot_loc) and check_not_wall(arr, next_robot_loc):
            ret_list.append(next_robot_loc)
    
    return ret_list


# 회전
def get_rotated_list(arr, robot_loc) -> list:
    
    ret_list = []
    
    [r1, c1], [r2, c2] = robot_loc
    # __    case: r1 == r2
    if r1 == r2:
        if r1 - 1 >= 0 and arr[r1 - 1][c1] != WALL and arr[r1 - 1][c2] != WALL:
            ret_list.append([[r1-1, c1], [r1, c1]])
            ret_list.append([[r1-1, c2], [r1, c2]])
        if r1 + 1 < LEN_BOARD and arr[r1 + 1][c1] != WALL and arr[r1 + 1][c2] != WALL:
            ret_list.append([[r1, c1], [r1+1, c1]])
            ret_list.append([[r1, c2], [r1+1, c2]])
    # |     case: c1 == c2
    else: 
        if c1 - 1 >= 0 and arr[r1][c1 - 1] != WALL and arr[r2][c1 - 1] != WALL:
            ret_list.append([[r1, c1-1], [r1, c1]])
            ret_list.append([[r2, c1-1], [r2, c1]])
        if c1 + 1 < LEN_BOARD and arr[r1][c1 + 1] != WALL and arr[r2][c1 + 1] != WALL:
            ret_list.append([[r1, c1], [r1, c1+1]])
            ret_list.append([[r2, c1], [r2, c1+1]])
        
    return ret_list


def bfs(arr):
    
    visited = [[[-1, -1] for _ in range(LEN_BOARD)] for _ in range(LEN_BOARD)]
    
    def check_end(robot_loc):
        return robot_loc[0] == [LEN_BOARD - 1, LEN_BOARD - 1] or robot_loc[1] == [LEN_BOARD - 1, LEN_BOARD - 1]

    def get_visited(robot_loc):
        [r1, c1], [r2, c2] = robot_loc
        if r1 != r2:
            return visited[min(r1, r2)][c1][1]
        else:
            return visited[r1][min(c1, c2)][0]
    
    def update_visited(robot_loc, val):
        [r1, c1], [r2, c2] = robot_loc
        if r1 != r2:
            visited[min(r1, r2)][c1][1] = val
        else:
            visited[r1][min(c1, c2)][0] = val
    
    start_loc = [[0, 0], [0, 1]]
    queue = [start_loc]
    update_visited(start_loc, 0)
    
    while queue:
        curr_loc = queue.pop(0)
        curr_visited = get_visited(curr_loc)
        
        
        
        if check_end(curr_loc):
            return curr_visited
        
        next_loc_list = get_moved_list(arr, curr_loc) + get_rotated_list(arr, curr_loc)
        for next_loc in next_loc_list:
            if not check_boundary(next_loc):
                print(next_loc)
                return
            if get_visited(next_loc) == -1:
                queue.append(next_loc)
                update_visited(next_loc, curr_visited + 1)                
    
    print("cannot reach")
    return -1
    
        
def solution(board):
    global LEN_BOARD
    
    answer = 0
    
    LEN_BOARD = len(board)
    answer = bfs(board)
    
    return answer
