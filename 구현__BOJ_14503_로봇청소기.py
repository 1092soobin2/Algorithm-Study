# 구현__BOJ_14503_로봇청소기
# 바운더리 조건 N,M인데 M,N이라고 함.

'''
NxM room
- wall(1) | empty(0)
- cleaned(2) | not cleaned

robot_cleaner
1. 현재 칸 청소
2. 인접 4칸 중 청소 X 빈 칸 O
    1. 방향을 유지한 채로 후진 -> 1번
    2. 후진할 수 없으면 멈춘다.
3. 인접 4칸 중 청소 X 빈 칸 X
    1. 반시계 90도 회전
    2. 바라보는 방향의 인접 칸이 청소X이면 전진
    3. 1번

ans: 청소하는 칸의 개수
'''





DIRECTION_LIST = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 북 -> 서 -> 남 -> 동
WALL, EMPTY, CLEANED_EMPTY = 1, 0, 2
# ===input===
N, M = map(int, input().split())
robot_r, robot_c, robot_direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 동, 서면 direction id 바꿔 주기
if robot_direction == 1:
    robot_direction = 3
elif robot_direction == 3:
    robot_direction = 1
# ===algorithm===


def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < M


def check_wall(arr, r, c):
    return arr[r][c] == WALL


def print_room(arr, r, c):
    for tr in range(N):
        for tc in range(M):
            if tr == r and tc == c:
                print("3", end=' ')
            else:
                print(arr[tr][tc], end=' ')
        print()
    print()


ans = 0
# robot r, c, d 업데이트 필요
while check_boundary(robot_r, robot_c) and not check_wall(room, robot_r, robot_c):
    # print_room(room, robot_r, robot_c)
    # 1. 현재 칸이 EMPTY && NOT_CLEANED
    if room[robot_r][robot_c] == EMPTY:
        room[robot_r][robot_c] = CLEANED_EMPTY
        ans += 1
    # 2. 인접 칸에 빈 칸 O
    flag_empty = False
    for i in range(1, 5):
        next_direction = (robot_direction + i) % 4
        dr, dc = DIRECTION_LIST[next_direction]
        nr, nc = robot_r+dr, robot_c+dc
        if check_boundary(nr, nc) and not check_wall(room, nr, nc) and room[nr][nc] == EMPTY:
            # print(f"MOVE: ({robot_r, robot_c}) -> ({nr, nc})")
            robot_r, robot_c, robot_direction = nr, nc, next_direction
            flag_empty = True
            break
    if flag_empty:
        continue
    # 3. 인접 칸에 빈 칸 X
    dr, dc = DIRECTION_LIST[(robot_direction + 2) % 4]
    # nr, nc = robot_r+dr, robot_c+dc
    # if check_boundary(nr, nc)
    robot_r, robot_c = robot_r+dr, robot_c+dc

# ===output===
print(ans)