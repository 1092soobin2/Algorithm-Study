import heapq


# N*M board
# P rabbit dict[id] -> [speed, jump_cnt, (r, c), score]
N, M = 0, 0
P = 0
rabbit_dict = dict()
jump_pq = []
SPEED, CNT, LOC = 0, 1, 2
SCORE = 3


def init():
    global rabbit_dict, N, M, P

    input_line = list(map(int, input().split()))
    N, M = input_line[1], input_line[2]
    P = input_line[3]

    # Make rabbit dictionary
    for p in range(P):
        rid, speed = input_line[4 + 2*p], input_line[4 + 2*p + 1]
        cnt, r, c, score = 0, 0, 0, 0
        rabbit_dict[rid] = [speed, cnt, [r, c], score]
        jump_pq.append((cnt, r + c, r, c, rid))

    heapq.heapify(jump_pq)


def play_game(repeat, bonus):
    global rabbit_dict, jump_pq

    jump_rabbit_set = set()
    total_score = 0

    def get_next_loc() -> list:
        loc, speed = rabbit_dict[rabbit_id][LOC], rabbit_dict[rabbit_id][SPEED]
        loc_pq = []

        def move_to(d: int, at: int, edge: int, go):

            while go > 0:
                if d == 1:
                    # (진행 가능 거리) >= (이동해야 하는 거리)
                    if (edge - 1 - at) >= go:
                        at += go
                        go = 0
                    else:
                        go -= (edge - 1 - at)
                        at = edge - 1
                        d = -1
                else:
                    if at >= go:
                        at -= go
                        go = 0
                    else:
                        go -= at
                        at = 0
                        d = 1
            return at

        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            # 다음 위치 구하기
            if dr != 0:
                nr, nc = move_to(dr, loc[0], N, speed % ((N - 1) * 2)), loc[1]
            else:
                nr, nc = loc[0], move_to(dc, loc[1], M, speed % ((M - 1) * 2))
            # 위치 우선 순위
            heapq.heappush(loc_pq, (-(nr + nc), -nr, -nc))

        return [-loc_pq[0][1], -loc_pq[0][2]]

    # 0. repeat
    for time in range(repeat):
        # 1. 점프할 토끼 선정
        # (jump_cnt, r+c, r, c, id)
        rabbit_info = heapq.heappop(jump_pq)
        rabbit_id = rabbit_info[-1]

        # 2. 점프할 위치 선정
        # (-(r+c), -r, -c)
        next_loc = get_next_loc()

        # 3. 점프하기
        jump_rabbit_set.add(rabbit_id)
        rabbit_dict[rabbit_id][CNT] += 1
        rabbit_dict[rabbit_id][LOC] = next_loc
        heapq.heappush(jump_pq, (rabbit_dict[rabbit_id][CNT], sum(next_loc), next_loc[0], next_loc[1], rabbit_id))

        # 3. 점수 업데이트
        # 점프한 토끼를 제외한 나머지 토끼가 (r + c)만큼의 점수를 얻게 됨

        # for rid in rabbit_dict:
        #     if rid == rabbit_id:
        #         continue
        #     rabbit_dict[rid][SCORE] += sum(next_loc) + 2
        total_score += sum(next_loc) + 2
        rabbit_dict[rabbit_id][SCORE] -= (sum(next_loc) + 2)

    # 3. 점수 업데이
    for rid in rabbit_dict:
        rabbit_dict[rid][SCORE] += total_score

    # 4. 종료  보너스 점수
    # (-(r + c), -r, -c, rid)
    bonus_pq = []
    for rid in jump_rabbit_set:
        r, c = rabbit_dict[rid][LOC]
        heapq.heappush(bonus_pq, (-(r + c), -r, -c, rid))

    rabbit_dict[bonus_pq[0][-1]][SCORE] += bonus


def modify_speed(rabbit_id, multiple):
    global rabbit_dict

    # n/a rabbit id가 주어지면 종료
    if rabbit_id not in rabbit_dict:
        print("n/a rabbit id")
        exit()

    # 이동 거리 변경
    rabbit_dict[rabbit_id][SPEED] = rabbit_dict[rabbit_id][SPEED] * multiple


# 최고의 토끼 선정 -> 가장 높은 점수
def finish():
    best_score = 0
    for rid in rabbit_dict:
        best_score = max(best_score, rabbit_dict[rid][SCORE])

    print(best_score)


def print_arr(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            print(f"{arr[r][c]:>2}", end=" ")
        print()


# algorithm
Q = int(input())
init()
for q in range(Q - 2):
    command, arg1, arg2 = map(int, input().split())
    if command == 200:
        play_game(arg1, arg2)
    elif command == 300:
        modify_speed(arg1, arg2)
    else:
        print("n/a command")
finish()
