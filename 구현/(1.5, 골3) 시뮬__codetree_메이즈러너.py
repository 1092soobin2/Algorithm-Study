# (1, 골3) 시뮬__codetree_메이즈러너


# N*N maze [1][1]~

# 빈칸
#
# 벽 [내구도 1~9]
# 회전 시마다 -1
# 내구도 0 -> 빈칸
#
# 출구


import heapq

# === input ===
N, M, K = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
# 참가자 [위치, 이동 거리]
players = [[list(map(lambda x: int(x) - 1, input().split())), 0] for _ in range(M)]
exit_loc = list(map(lambda x: int(x) - 1, input().split()))
LOC, DIST = 0, 1


# 1. 1초마다 움직인다
def move_players():
    global players, answer

    new_players = []
    for player in players:
        loc_pq = []
        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nr, nc = player[LOC][0] + dr, player[LOC][1] + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] == 0:
                # 출구까지의 거리가 더 가까운 곳
                dist = abs(exit_loc[0]-player[LOC][0]) + abs(exit_loc[1]-player[LOC][1])
                ndist = abs(exit_loc[0]-nr) + abs(exit_loc[1]-nc)
                # 상하 -> 좌우
                if ndist < dist:
                    heapq.heappush(loc_pq, (ndist, abs(dc), [nr, nc]))
        # 움직일 수 없으면 움직이지 X
        if loc_pq:
            player[LOC] = loc_pq[0][2]
            # answer += loc_pq[0][0]
            answer += 1

        if player[LOC] != exit_loc:
            new_players.append(player)

    players = new_players
    # TODO: return 후에 players가 empty면 게임 종료


# 2. 미로 회전
def rotate_maze():
    global maze, players, exit_loc

    def rotate_clockwise(sr, sc, e):
        global exit_loc, players
        e = e + 1

        # 시계 90도 회전, 내구도 -1
        player_arr = [[list() for _ in range(e)] for _ in range(e)]
        new_players = []
        for player in players:
            if sr <= player[LOC][0] <= sr + edge and sc <= player[LOC][1] <= sc + edge:
                player_arr[player[LOC][0] - sr][player[LOC][1] - sc].append(player[DIST])
            else:
                new_players.append(player)

        new_player_arr = [[list() for _ in range(e)] for _ in range(e)]
        new_arr = [[0]*e for _ in range(e)]
        for r in range(e):
            for c in range(e):
                new_player_arr[c][e - 1 - r] = player_arr[r][c][:]
                new_arr[c][e - 1 - r] = maze[r + sr][c + sc]

        for r in range(e):
            break_flag = False
            for c in range(e):
                if [sr + r, sc + c] == exit_loc:
                    exit_loc = [sr + c, sc + e - 1 - r]
                    break_flag = True
                    break
            if break_flag:
                break

        for r in range(e):
            for c in range(e):
                if new_player_arr[r][c]:
                    for new_player in new_player_arr[r][c]:
                        new_players.append([[r + sr, c + sc], new_player])
                if new_arr[r][c] > 0:
                    new_arr[r][c] -= 1
                maze[r + sr][c + sc] = new_arr[r][c]

        players = new_players

    # 한명 이상의 참가자와 출구를 포함한 가장 작은 정사각형
    sq_pq = []
    for player in players:
        edge = max(abs(player[LOC][0]-exit_loc[0]), abs(player[LOC][1]-exit_loc[1]))
        # 2개 이상이면 min r -> min c
        cand_r, cand_c = max(player[LOC][0], exit_loc[0]) - edge, max(player[LOC][1], exit_loc[1]) - edge
        heapq.heappush(sq_pq, (edge, max(cand_r, 0), max(cand_c, 0)))

    # maze 회전
    edge, start_r, start_c = sq_pq[0]
    rotate_clockwise(start_r, start_c, edge)


# 3. repeat K
# K 전에 모두 탈출 하면 게임 종료
answer = 0
for _ in range(K):
    move_players()
    if not players:
        break
    rotate_maze()

    # print(answer)
    # print(players)
    # print(exit_loc)
    # for r in range(N):
    #     print(*maze[r])
    # print("\n")

# 게임 종료 시 sum(이동거리) , 출구 좌표
print(answer)
print(exit_loc[0] + 1, exit_loc[1] + 1)
