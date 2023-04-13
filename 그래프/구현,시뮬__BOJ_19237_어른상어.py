# 구현,시뮬__BOJ_19237_어른상어

'''
N x N 격자
M 칸에 상어

상어
- unique 번호를 가짐
- 한 칸을 사수함
- 1 > 2 > 3 > ...

- 냄새를 뿌린다. (k초 후까지 유효)
- 1초마다 인접(상하좌우) 칸으로 이동

- 이동 방향 결정
    - 아무 냄새 없는 칸
    - 자기 냄새가 있는 칸
'''




# ===input===
N, M, k = map(int, input().split())


DIRECTION_TUP = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
# space: 냄새[상어 번호, 유효 시간], 상어[1, 2, ..]
class Space:
    def __init__(self):
        self.shark_id_list = []
        self.smell_num = 0
        self.smell_time = 0

    def initial_shark(self, shark):
        self.shark_id_list = [shark]
        self.smell_num = shark
        self.smell_time = k

    def add_new_shark(self, shark_id):
        self.shark_id_list.append(shark_id)

    def remove_shark(self, shark_id):
        self.shark_id_list.remove(shark_id)

    # TODO: 여러 마리인 경우 고려했는지? 00
    # TODO: 냄새 update 함?
    def is_smell(self):
        return self.smell_time != 0

    def whose_smell(self):
        return self.smell_num

    # TODO: 리턴값 sharks 리스트에 업데이트 필요
    def flow_1second_and_who_is_dead(self) -> list:
        dead = []
        if len(self.shark_id_list) == 1:
            self.smell_num = self.shark_id_list[0]
            self.smell_time = k
        elif self.smell_time == 0 and len(self.shark_id_list) > 1:
            self.shark_id_list.sort()
            dead = self.shark_id_list[1:]
            self.shark_id_list = self.shark_id_list[0:1]
            self.smell_time = k
            self.smell_num = self.shark_id_list[0]
        elif self.smell_time > 0:
            self.smell_time -= 1

        return dead


class Shark:
    def __init__(self, i):
        self.id = i
        self.direction_id = 0
        self.priority_list = [[]]
        self.row, self.col = 0, 0

    def get_location(self):
        return self.row, self.col

    def update_location(self, r, c):
        self.row, self.col = r, c

    # TODO: 리턴된 값을 spaces에 업데이트 해줘야 함.
    def move_to(self, arr) -> (int, int):
        # 냄새 없는 칸
        for next_d_id in self.priority_list[self.direction_id]:
            dr, dc = DIRECTION_TUP[next_d_id]
            nr, nc = self.row+dr, self.col+dc
            # print(f"next did: {next_d_id}, next location: {nr},{nc}")
            if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc].is_smell():
                self.direction_id = next_d_id
                self.update_location(nr, nc)
                return nr, nc

        # 자기 냄새인 칸
        for next_d_id in self.priority_list[self.direction_id]:
            dr, dc = DIRECTION_TUP[next_d_id]
            nr, nc = self.row + dr, self.col + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc].whose_smell() == self.id:
                self.direction_id = next_d_id
                self.update_location(nr, nc)
                return nr, nc

        print("There is no way.")
        exit()


spaces = [list(Space() for _ in range(N)) for _ in range(N)]
sharks = [Shark(i) for i in range(0, M + 1)]
sharks[0] = None

def print_spaces():
    print("=============")
    for i in range(N):
        for space in spaces[i]:
            sid = space.shark_id_list
            s_t = space.smell_time
            s_n = space.smell_num if s_t != 0 else 0
            additional = f"({s_t},{s_n})" if s_t != 0 else "     "
            print(sid, additional, end='')
        print()
    print("=============\n")


# N줄 지도
tmp_input = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if tmp_input[i][j] != 0:
            spaces[i][j].initial_shark(tmp_input[i][j])
            sharks[tmp_input[i][j]].update_location(i, j)

# 방향
tmp_input = list(map(int, input().split()))
for i in range(1, M+1):
    sharks[i].direction_id = tmp_input[i-1]

# 우선 순위 리스트
# priority_list[상하좌우(0, 1, 2, 3, 4)] = 1,
priority_list = [list() for i in range(M)]
for i in range(1, M+1):
    for _ in range(4):
        sharks[i].priority_list.append(list(map(int, input().split())))


# ===algorithm===
def move_in_1second():
    # 상어 이동
    for shark in sharks:
        if shark is not None:
            from_r, from_c = shark.get_location()
            to_r, to_c = shark.move_to(spaces)
            # print(f"shark_id: {shark.id}, {from_r},{from_c} -> {to_r},{to_c}")
            # print_spaces()
            spaces[from_r][from_c].remove_shark(shark.id)
            spaces[to_r][to_c].add_new_shark(shark.id)

    # 공간 업데이트
    for i in range(N):
        for j in range(N):
            dead = spaces[i][j].flow_1second_and_who_is_dead()
            for shark_id in dead:
                sharks[shark_id] = None

    # print_spaces()


def is_done() -> bool:
    for shark_id in range(2, M + 1):
        if sharks[shark_id] is not None:
            return True
    return False


# ===output===
ans = 0
while is_done() and ans != 1001:
    move_in_1second()
    ans += 1

# print(ans)

if ans > 1000:
    print("-1")
else:
    print(ans)
