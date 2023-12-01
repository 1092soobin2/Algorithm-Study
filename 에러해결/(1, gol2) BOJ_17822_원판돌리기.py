# (1, gol2) BOJ_17822_원판돌리기

# 반지름이 1, 2, ..., N인 원판
# (i,j) adj -> (i, j-1), (i, j+1), (i-1,j) (i+1),j

# 원판에 수가 남아 있으면, 인접하면서 같은 수 찾아서
    # 1) 모두 지움.
    # 2) 없는 경우 평균 +-1

# 15:30~

from collections import deque
import sys
sys.setrecursionlimit(20000000)


CLOCKWISE, COUNTER_CLOCKWISE = 0, 1


def rotate(circle: deque, direction, speed):
    for _ in range(speed):
        if direction == CLOCKWISE:
            circle.appendleft(circle.pop())
        else:
            circle.append(circle.popleft())


def bfs(start):
    global circle_list

    visited = {tuple(start)}
    queue = deque([start])
    criteria = circle_list[start[0]][start[1]]
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nr, nc = r + dr, (c + dc) % M
            if 0 <= nr < N and circle_list[nr][nc] == criteria and (nr, nc) not in visited:
                queue.append([nr, nc])
                visited.add((nr, nc))

    if len(visited) > 1:
        for r, c in list(visited):
            circle_list[r][c] = 0
        return True
    else:
        return False


def check_circle():
    global circle_list

    erased = False
    for r in range(N):
        for c in range(M):
            if circle_list[r][c] != 0:
                erased |= bfs((r, c))

    if not erased:
        summ, numm = 0, 0
        for r in range(N):
            for c in range(M):
                if circle_list[r][c] != 0:
                    summ += circle_list[r][c]
                    numm += 1
        if not numm == 0:
            avg = summ / numm
            for r in range(N):
                for c in range(M):
                    if circle_list[r][c] == 0:
                        continue
                    if circle_list[r][c] > avg:
                        circle_list[r][c] -= 1
                    elif circle_list[r][c] < avg:
                        circle_list[r][c] += 1
            return True
        else:
            return False
    else:
        return True


# ===
N, M, T = map(int, input().split())
circle_list = [deque(map(int, input().split())) for _ in range(N)]
rotation_list = [list(map(int, input().split())) for _ in range(T)]


# ===
def solution():

    for x, d, k in rotation_list:
        for i in range(x-1, N, x):
            rotate(circle_list[i], d, k)
        print_debug("rotation")
        if not check_circle():
            break
        print_debug("erase")

    return sum(map(sum, circle_list))


def print_debug(title=""):
    if not DEBUG:
        return

    print("=====" + title)
    for r in range(N):
        for c in range(M):
            if circle_list[r][c] == 0:
                print("_", end="")
            else:
                print(circle_list[r][c], end="")
        print()
    print("=====")


# ===
DEBUG = True
DEBUG = False
print(solution())
