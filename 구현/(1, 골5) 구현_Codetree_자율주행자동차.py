# (1, 골5) _Codetree_자율주행자동차

# === input ===
N, M = map(int, input().split())
car_info = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]


# === algorithm ===
ROAD, SIDEWALK = 0, 1


def drive():

    ret_int = 0
    direction_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북, 동, 남, 서

    # D S
    visited = [[False]*M for _ in range(N)]

    def get_next_info(info):
        r, c, d = info
        for i in range(1, 5):
            nd = (d - i) % 4
            dr, dc = direction_list[nd]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == ROAD:
                    return [nr, nc, nd]
        return info

    def reverse(info):
        r, c, d = info
        dr, dc = direction_list[d]
        nr, nc = r - dr, c - dc
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == ROAD:
            return [nr, nc, d]
        return info


    # 출발점
    curr_info = car_info
    ret_int += 1
    visited[curr_info[0]][curr_info[1]] = True
    next_info = get_next_info(curr_info)

    while curr_info != next_info:

        if debug:
            print(curr_info, next_info)

        curr_info = next_info
        if not visited[curr_info[0]][next_info[1]]:
            ret_int += 1
        visited[curr_info[0]][curr_info[1]] = True

        # 1. 좌 == not visited -> 좌회전 + 1칸 전진
        # 2. 좌 == 인도 or visited -> 좌회전 + 1번 과정
        next_info = get_next_info(curr_info)
        # 3. 2번에서 이동 불가능 -> 현 방향으로 후진 + 1번 과정
        if next_info == curr_info:
            next_info = reverse(curr_info)

        # 4. 3번에서 이동 불가능 -> 작동 멈춤

    return ret_int


# === output ===
# ans: 자동차가 움직인 면적
debug = False
print(drive())
