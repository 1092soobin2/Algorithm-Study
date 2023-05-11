# ( 골1) __codetree_포탑부수기


# N * M grid

# 각 포탑 [공격력, 공격 시점]
# - 공격력 <= 0 이면 부서짐)

# === input ===
N, M, K = map(int, input().split())
board = [list(map(lambda x: [int(x), 0], input().split())) for _ in range(N)]
WALL = 0
POWER, TIME = 0, 1


# === algorithm ===
# 하나의 턴
# 1. 공격자 선정: 가장 약한 포탑 + (N+M)
def find_weakest() -> list:
    ret_loc = [0, 0]
    weakest = [1e9, 0]

    for r in range(N):
        for c in range(M):
            flag = False
            # 0) 벽이면 패스
            if board[r][c] == WALL:
                continue
            # 1) 공격력이 가장 낮은
            if board[r][c][POWER] < weakest[POWER]:
                flag = True
            elif board[r][c][POWER] == weakest[POWER]:
                # 2) 가장 최근에 공격한
                if board[r][c][TIME] > weakest[TIME]:
                    flag = True
                # 3) 행 + 열이 가장 큰
                elif board[r][c][TIME] == weakest[TIME]:
                    if (r + c) > sum(ret_loc):
                        flag = True
                    elif (r + c) == sum(ret_loc):
                        # 4) 열이 가장 큰
                        if c > ret_loc[1]:
                            flag = True

            if flag:
                ret_loc = [r, c]
                weakest = board[r][c]

    return ret_loc


# 2. 피해자 선정: 가장 강한 포탑
def find_strongest(weakest_loc) -> list:
    ret_loc = [-1, -1]
    strongest = [0, 1e9]

    for r in range(N):
        for c in range(M):
            # 0) 벽이면 패스
            if board[r][c] == WALL:
                continue

            # 0) 공격자이면 패스
            if [r, c] == list(weakest_loc):
                continue

            flag = False
            # 1) 공격력 max
            if board[r][c][POWER] > strongest[POWER]:
                flag = True
            elif board[r][c][POWER] == strongest[POWER]:
                # 2) 가장 예전에 공격한
                if board[r][c][TIME] < strongest[TIME]:
                    flag = True
                # 3) 행 + 열 min
                elif board[r][c][TIME] == strongest[TIME]:
                    if (r + c) < sum(ret_loc):
                        flag = True
                    elif (r + c) == sum(ret_loc):
                        # 4) 열이 가장 큰
                        # 4) 열 min
                        if c < ret_loc[1]:
                            flag = True

            if flag:
                ret_loc = [r, c]
                strongest = board[r][c]

    return ret_loc


# 2.1. 공격
def attack(weakest_loc, strongest_loc, time) -> set:
    global board

    ret_set = set()         # 공격자 + 피해자 리스트

    def find_shortest_path() -> list:
        # 1) 우 -> 하 -> 좌 -> 상 [[0, 1], [-1, 0], [0, -1], [1, 0]]
        # 2) 부서진 포탑은 지날 수 없다
        # 3) 양 끝은 이어져 있다.
        ret_list = []

        queue = [weakest_loc]
        path = [[list() for _ in range(M)] for _ in range(N)]
        path[weakest_loc[0]][weakest_loc[1]] = [weakest_loc]

        while queue:
            r, c = queue.pop(0)
            curr_path = path[r][c]
            if [r, c] == list(strongest_loc):
                ret_list = curr_path[1:]

            for dr, dc in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
                nr, nc = (r + dr) % N, (c + dc) % M
                if board[nr][nc] != WALL and path[nr][nc] == []:
                    queue.append([nr, nc])
                    path[nr][nc] = curr_path + [[nr, nc]]

        return ret_list

    def laser(path):
        power = board[weakest_loc[0]][weakest_loc[1]][POWER]
        for r, c in path:
            ret_set.add((r, c))
            # 1) 공격 대상 -= (공격력)
            if [r, c] == list(strongest_loc):
                board[r][c][POWER] -= power
            # 2) 레이저 경로 -= (공격력 // 2)
            else:
                board[r][c][POWER] -= (power // 2)

    def bomb():
        power = board[weakest_loc[0]][weakest_loc[1]][POWER]
        # 1) 공격 대상 -= (공격력)
        ret_set.add(tuple(strongest_loc))
        board[strongest_loc[0]][strongest_loc[1]][POWER] -= power
        # 2) 주변 8개 -= (공격력 // 2)
        for dr, dc in [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]:
            r, c = (strongest_loc[0] + dr) % N, (strongest_loc[1] + dc) % M
            if board[r][c] == WALL:
                continue
            if [r, c] == list(weakest_loc):
                continue
            ret_set.add((r, c))
            board[r][c][POWER] -= (power // 2)

    # 공격자 업데이트
    board[weakest_loc[0]][weakest_loc[1]][POWER] += (N + M)
    board[weakest_loc[0]][weakest_loc[1]][TIME] = time

    # 공격
    ret_set.add(tuple(weakest_loc))
    shortest_path = find_shortest_path()
    # 2-1. 레이저 공격: 최단 경로가 존재하는 경우
    if shortest_path:
        laser(shortest_path)
    # 2-2. 포탄 공격: 최단 경로 X
    else:
        bomb()

    return ret_set


# 3. 포탑 부서짐: 0 이하인 탑은 0으로
def destroy():
    global board
    for r in range(N):
        for c in range(M):
            # 벽이면 패스
            if board[r][c] == WALL:
                continue

            # 0 이하면 벽으로 만들어 주기
            if board[r][c][POWER] <= 0:
                board[r][c] = WALL


# 4. 포탑 정비
def heal(members):
    for r in range(N):
        for c in range(M):
            # 1) 부서지지 않은 포탑 중
            if board[r][c] == WALL:
                continue
            # 2) 공격자X, 피해자X
            if (r, c) in members:
                continue
            # 3) -> 공격력 1
            board[r][c][POWER] += 1


def one_round(ith) -> bool:
    weakest_loc = find_weakest()
    strongest_loc = find_strongest(weakest_loc)
    # 1명 남으면 종료
    if strongest_loc == [-1, -1]:
        return False

    member_set = attack(weakest_loc, strongest_loc, ith)
    destroy()
    heal(member_set)

    # print(f"\nw: {weakest_loc}, s: {strongest_loc}")
    # for r in range(N):
    #     print(*board[r])

    return True


def get_strongest_power() -> int:
    ret_int = 0

    for r in range(N):
        for c in range(M):
            if board[r][c] == WALL:
                continue

            ret_int = max(ret_int, board[r][c][POWER])

    return ret_int


# === output ===
# K 라운드 진행
destroy()
for k in range(K):
    if not one_round(k + 1):
        break

# 가장 강한 포탑의 공격력
print(get_strongest_power())
