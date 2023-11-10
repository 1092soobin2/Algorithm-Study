# (0.5, 골2) BOJ_17822_원판돌리기


# 1 2 3 4 1 2 3 4
# 1-M -> (1,i) 는 (1,i-1), (1,i+1)과 근접함
# 1-N -> (2,i) 는 (1,i), (3,i)과 근접함 1123 ->(clock, 3) 1231 (counter, 3) -> 3112
#                                           (clock, 1) 3112 (counter, 1) -> 1231

# 총 T번  회전시킴

# answer: T 회전 후 sum(적힌 수)

from collections import deque


class Board:
    CLOCKWISE, COUNTER_CLOCKWISE = 0, 1
    disk = []
    ROTATION_INFO_LIST = []

    @classmethod
    def _get_adj(cls):

        visited = [[False] * M for _ in range(N)]

        def bfs(start) -> list:
            sr, sc = start
            if cls.disk[sr][sc] == 0:
                return []

            queue = deque([start])
            acc = set([(sr, sc)])
            visited[sr][sc] = True

            while queue:
                curr_r, curr_c = queue.popleft()

                adj_loc = [[curr_r, (curr_c - 1) % M], [curr_r, (curr_c + 1) % M]]
                if curr_r == 0:
                    adj_loc.append([1, curr_c])
                elif curr_r == M - 1:
                    adj_loc.append([M - 2, curr_c])
                else:
                    adj_loc += [[curr_r - 1, curr_c], [curr_r + 1, curr_c]]

                for nr, nc in adj_loc:
                    if cls.disk[nr][nc] == cls.disk[sr][sc] and not visited[nr][nc]:
                        queue.append([nr, nc])
                        visited[nr][nc] = True
                        acc.add((nr, nc))
            return list(acc) if len(acc) != 1 else []

        adj_list = []
        for r in range(N):
            for c in range(M):
                if not visited[r][c] and cls.disk[r][c] != 0:
                    adj = bfs([r, c])
                    if adj:
                        adj_list += adj

        return adj_list

    @classmethod
    def _get_avg(cls):
        num_disk = N * M - sum(map(lambda x: x.count(0), cls.disk))
        sum_disk = sum(map(sum, cls.disk))
        return sum_disk / num_disk

    @classmethod
    def rotate(cls, x, d, k):
        # 회전 방법은 미리 정해져 있음 (x, d, k)

        # 1. x의 배수의 원판, d(0-시계,1-반시계) k칸 회전
        for disk_num in range(x, N + 1, x):
            i = disk_num - 1
            if d == cls.CLOCKWISE:
                cls.disk[i] = cls.disk[i][M-k:] + cls.disk[i][:M-k]
            else:
                cls.disk[i] = cls.disk[i][k:] + cls.disk[i][:k]

        # 2. 원판에 수가 남아 잇으면, 인접하면서 수가 같은 것을 모두 찾는다
        to_be_removed = cls._get_adj()
        # 1) 수 존재 O -> 모두 지운다
        if to_be_removed:
            for r, c in to_be_removed:
                cls.disk[r][c] = 0
        # 2) 수 존재 X -> 원판에 적힌 수의 평균을 구하여, 평균 보다 큰 수에느 -1, 작은 수에는 + 1
        else:
            avg = cls._get_avg()
            for r in range(N):
                for c in range(M):
                    if cls.disk[r][c] == 0:
                        continue
                    elif cls.disk[r][c] > avg:
                        cls.disk[r][c] -= 1
                    elif cls.disk[r][c] < avg:
                        cls.disk[r][c] += 1


# === input ===
N, M, T = map(int, input().split())
Board.disk = [list(map(int, input().split())) for _ in range(N)]
Board.ROTATION_INFO_LIST = [list(map(int, input().split())) for _ in range(T)]


# === algorithm ===
def solution():
    for i in range(T):
        Board.rotate(*Board.ROTATION_INFO_LIST[i])

    return sum(map(sum, Board.disk))


# === output ===
print(solution())


