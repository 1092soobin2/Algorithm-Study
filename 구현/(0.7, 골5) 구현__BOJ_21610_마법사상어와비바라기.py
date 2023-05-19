# (0.7, 골5) 구현__BOJ_21610_마법사상어와비바라기

# N*N board [물의양]

# 비바라기 시전
# [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)] 에 비구름이 생김
# M번 이동 명령 (d, s)


# M번 후 sum(물의양)

# ===input===
DIRECTION_LIST = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
N, M = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
sky = [[0]*N for _ in range(N)]


# ===algorithm===
sky[N-2][0], sky[N-2][1], sky[N-1][0], sky[N-1][1] = 1, 1, 1, 1


def one_round(direction, speed):
    global sky, ground
    new_sky = [[0] * N for _ in range(N)]

    # 1. 모든 구름이 d로 s만큼 이동
    dr, dc = DIRECTION_LIST[direction]
    for r in range(N):
        for c in range(N):
            if sky[r][c] != 0:
                nr, nc = (r + dr * speed) % N, (c + dc * speed) % N
                new_sky[nr][nc] = sky[r][c]

    # 2. 구름 칸의 물의양 +1
    for r in range(N):
        for c in range(N):
            if new_sky[r][c] != 0:
                ground[r][c] += 1

    # 4. 2에서 증가한 칸에 물복사 버그
    for r in range(N):
        for c in range(N):
            if new_sky[r][c] != 0:
                # 1) 대각선 방향으로 거리가 1인칸에 물이 있는 바구니의 수만큼 바구니 물의 양이 증가
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    # 2) 이동과 다르게 경계를 넘어가는 칸은 거리가 1인 칸이 아니다.
                    if 0 <= nr < N and 0 <= nc < N and ground[nr][nc] > 0:
                        ground[r][c] += 1

    # 5. 물의양 >=2 인 칸에 구름이 생기고, 물의 양이 2 줄어든다. (3에서 구름이 사라진 칸이 아니어야 한다.)
    for r in range(N):
        for c in range(N):
            # 3. 구름이 사라짐
            if new_sky[r][c] != 0:
                new_sky[r][c] = 0
            else:
                if ground[r][c] >= 2:
                    new_sky[r][c] = 1
                    ground[r][c] -= 2

    sky = new_sky


def print_arr(arr):
    for r in range(N):
        print(*arr[r])
    print()


# ===output===
for _ in range(M):
    d, s = map(int, input().split())
    one_round(d, s)

print(sum(map(sum, ground)))
