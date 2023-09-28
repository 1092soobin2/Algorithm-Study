# (0.5, 골4) BOJ_14891_톱니바퀴

# 23:23~

# 8개 톱니 [N | S]
# 4개 톱니바퀴 (1번 - 2번 - 3번 - 4번)

# K번 회전
# 한 칸 기준
# 시계 | 반시계 방향
#    0
#  7   1
# 6     2
#  5   3
#    4

# 회전
# 1. 회전시킬 톱니바퀴
# 2. 회전시킬 방향

# 서로 맞닿은 극
# N/S or S/N -> 반대 방향으로 회전
# N/N or S/S


# === input ===
wheel_list = [input() for _ in range(4)]
NORTH, SOUTH = '0', '1'
K = int(input())
ROTATION_LIST = [list(map(int, input().split())) for _ in range(K)]
CLOCKWISE = 1


# === algorithm ===
def rotate_one_wheel(wheel_idx, direction):
    if direction == CLOCKWISE:
        return wheel_list[wheel_idx][7] + wheel_list[wheel_idx][:7]
    else:
        return wheel_list[wheel_idx][1:] + wheel_list[wheel_idx][0]


def rotate(wheel_idx, direction):
    global wheel_list

    queue = [[wheel_idx, direction]]
    visited = [False]*4
    visited[wheel_idx] = True

    while queue:
        curr_wheel_idx, curr_d = queue.pop(0)

        left_idx, right_idx = curr_wheel_idx - 1, curr_wheel_idx + 1
        if 0 <= left_idx < 4 and not visited[left_idx]:
            if wheel_list[left_idx][2] != wheel_list[curr_wheel_idx][6]:
                queue.append([left_idx, -1 * curr_d])
                visited[left_idx] = True
        if 0 <= right_idx < 4 and not visited[right_idx]:
            if wheel_list[curr_wheel_idx][2] != wheel_list[right_idx][6]:
                queue.append([right_idx, -1 * curr_d])
                visited[right_idx] = True
        wheel_list[curr_wheel_idx] = rotate_one_wheel(curr_wheel_idx, curr_d)


def solution():
    for wheel_num, direction in ROTATION_LIST:
        rotate(wheel_num - 1, direction)

    return sum([(2**i) * int(wheel_list[i][0]) for i in range(4)])


# === output ===
print(solution())
