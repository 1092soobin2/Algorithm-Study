# (1, 골1) __Codetree_꼬리잡기놀이

# n*n grid

# 3명 이상 한 팀 [이동선, 사람 수]
# 공을 맞는 첫 번쨰 사람 팀이 점수 획득 -> 팀 내의 번호 k, k^2만큼 점수 획득
# 점수 획득 팀은 방향을 바꿈

# === input ===
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
group_list = []         # [방향, 사람들]
EMPTY, HEAD, REST, TAIL, ROAD = 0, 1, 2, 3, 4


# === algorithm ===
def init():
    global group_list

    def dfs(start):

        new_group = []
        visited = [[False]*n for _ in range(n)]

        curr = start
        while board[curr[0]][curr[1]] != ROAD and not visited[curr[0]][curr[1]]:
            new_group.append(curr)
            visited[curr[0]][curr[1]] = True
            for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]\
                        and 0 <= board[nr][nc] - board[curr[0]][curr[1]] <= 1:
                    curr = [nr, nc]
                    break

        return new_group

    for r in range(n):
        for c in range(n):
            if board[r][c] == HEAD:
                group = [1, dfs([r, c])]
                group_list.append(group)


# 1. 한 칸 이동
def move_one():
    global board, group_list

    for [direction, people] in group_list:
        head = 0 if direction == 1 else len(people) - 1
        tail = len(people) if direction == 1 else -1

        # 머리 사람의 이동할 칸
        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nr, nc = people[head][0] + dr, people[head][1] + dc
            if 0 <= nr < n and 0 <= nc < n and (board[nr][nc] == ROAD or board[nr][nc] == HEAD or board[nr][nc] == TAIL):
                next_loc = [nr, nc]
                break

        # 앞 사람 칸으로 이동
        for i in range(head, tail - direction, direction):
            nr, nc = next_loc
            # update board
            board[nr][nc] = board[people[i][0]][people[i][1]]
            # update next_loc
            next_loc = people[i]
            # update group_list
            people[i] = [nr, nc]

        # 마지막 칸
        if people[tail - direction] == people[head]:
            board[next_loc[0]][next_loc[1]] = TAIL if direction == 1 else HEAD
        else:
            board[next_loc[0]][next_loc[1]] = board[people[tail - direction][0]][people[tail - direction][1]]
            board[people[tail - direction][0]][people[tail - direction][1]] = ROAD
        people[tail - direction] = next_loc


# 2. 공 던져짐
def throw_ball(time) -> int:
    # 1초부터 시작
    time = time % (4 * n)
    time = 4 * n if time == 0 else time

    if 0 < time <= n:
        start = [time - 1, 0]
        dr, dc = 0, 1
    elif n < time <= 2 * n:
        start = [n - 1, time - 1 - n]
        dr, dc = -1, 0
    elif 2 * n < time <= 3 * n:
        start = [n - (time - 2 * n), n - 1]
        dr, dc = 0, -1
    elif 3 * n < time <= 4 * n:
        start = [0, n - (time - 3 * n)]
        dr, dc = 1, 0
    else:
        return

    r, c = start
    if debug:
        print(start)
        print_board()
    for _ in range(n):
        # 빈 칸이 아니고 길이 아니면 (-> 사람이면)
        if board[r][c] != EMPTY and board[r][c] != ROAD:
            for i, [direction, people] in enumerate(group_list):
                # 속한 group 찾기
                if [r, c] in people:
                    # 순서 구하기
                    if direction == 1:
                        order = people.index([r, c]) + 1
                    else:
                        order = len(people) - people.index([r, c])

                    group_list[i][0] *= -1

                    if debug:
                        print([r, c], people, order)
                    return order * order
        r, c = r + dr, c + dc

    # 아무도 볼을 못 잡으면 지나간다.
    return 0


def print_board():
    print(group_list)
    for r in range(n):
        print(*board[r])
    print()


# === output ===
init()

# ans: 점수 총합
debug = False
answer = 0
for t in range(k):
    move_one()
    answer += throw_ball(t + 1)
    if debug:
        print(answer)
        print("======================")
print(answer)
