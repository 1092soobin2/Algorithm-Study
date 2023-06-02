# (1, 골5) Codetree_돌아가는팔각의자


# 4개의 팔각 의자
# 사람 N | S




# === input ===
seat_list = [list(map(int, input())) for _ in range(4)]     # [12시부터 시계 방향]
K = int(input())
command_list = [list(map(int, input().split())) for _ in range(K)]

NORTH, SOUTH = 0, 1
CLOCKWISE, COUNTER_CLOCKWISE = 1, -1


# === algorithm ===
def rotate(number, direction):
    # 회전 요청 [의자 번호, 방향]

    global seat_list

    def rotate_one(itr, d):
        # 각각의 의자를 k번 회전 시킴
        # 한 번 회전 -> 45도씩 한 칸

        if d == CLOCKWISE:
            seat_list[itr] = seat_list[itr][-1:] + seat_list[itr][:-1]
        else:
            seat_list[itr] = seat_list[itr][1:] + seat_list[itr][:1]

    # n 의자 회전하기 전
        # 인접 의자 (n-1, n+1)에서 제일 가까운 2명의 출신 지역 != -> 반대 방향 회전
        # 모든 회전이 끝날 때까지 기다림.
        # 이 과정에서 한 의자는 1번만 회전함

    command_dict = dict()

    # 시작
    queue = [number-1]
    command_dict[number-1] = direction

    # 연쇄 회전
    while queue:
        curr = queue.pop(0)
        if debug:
            print(curr)
        # n-1 seat
        if curr > 0 and (curr - 1) not in command_dict:
            # [n-1][2] == [n][6]
            if seat_list[curr - 1][2] != seat_list[curr][6]:
                command_dict[curr - 1] = command_dict[curr] * -1
                queue.append(curr - 1)
        # n + 1 seat
        if curr < 3 and (curr + 1) not in command_dict:
            # [n][2] == [n+1][6]
            if seat_list[curr][2] != seat_list[curr + 1][6]:
                command_dict[curr + 1] = command_dict[curr] * -1
                queue.append(curr + 1)

    for i in command_dict:
        rotate_one(i, command_dict[i])

    if debug:
        print(command_dict)
        print_debug()


def print_debug():
    for i in range(4):
        print(*seat_list[i])


def get_ans():
    return 1 * seat_list[0][0] + 2 * seat_list[1][0] + 4 * seat_list[2][0] + 8 * seat_list[3][0]


# === output ===
debug = False
for command in command_list:
    rotate(*command)
print(get_ans())

# ans: 12시 방향 s값 여부 (1, 0)
# 1*s1 + 2+s2 + 4+s3 + 8+s4

