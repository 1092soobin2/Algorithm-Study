# 구현__BOJ_21608_상어초등하교 09:45~
'''
NxN classroom (1,1) - (N,N)
NxN students

1. 빈 칸 중에 좋아하는 학생이 가장 많이 인접한 칸
2. 인접한 칸 중에 빈 칸이 가장 많은 칸
3. 행의 번호가 가장 작은 칸
4. 열의 번호가 가장 작은 칸

만족도: 인접한 칸에 앉은 좋아하는 학생 수
'''

# ===input===
N = int(input())
students = list()
preference_dict = dict()
for _ in range(N * N):
    tmp_list = list(map(int, input().split()))
    students.append(tmp_list[0])
    preference_dict[tmp_list[0]] = tmp_list[1:]


# ===algorithm===
# DIRECTION_LIST =
def count_like(room, r, c, student_id):
    like = 0
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dr, c + dc
        if check_room(nr, nc) and room[nr][nc] in preference_dict[student_id]:
            like += 1
    return like


def count_empty(room, r, c):
    empty = 0
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dr, c + dc
        if check_room(nr, nc) and room[nr][nc] == 0:
            empty += 1
    return empty


def check_room(r, c):
    return 0 <= r < N and 0 <= c < N


def print_room(room):
    for i in range(N):
        for j in range(N):
            print(room[i][j], end=' ')
        print()

# 1. 자리 배치
def make_classroom() -> list:
    room = [[0]*N for _ in range(N)]

    def decide_position(student_id: int) -> (int, int):
        positions = list()      # [like 개수, empty 개수, position]

        for r in range(N):
            for c in range(N):
                if room[r][c] == 0:
                    like = count_like(room, r, c, student_id)
                    empty = count_empty(room, r, c)
                    positions.append([like, empty, (r, c)])

        positions.sort(key=lambda x: (-x[0], -x[1], x[2][0], x[2][1]))
        return positions[0][2]

    room[1][1] = students[0]
    for student in students[1:]:
        r, c = decide_position(student)
        room[r][c] = student

    return room


# 2. 만족도 계산
def cal_satisfaction(room):
    satisfaction = [0, 1, 10, 100, 1000]    # 0, 1, 2, 3, 4
    total = 0

    for r in range(N):
        for c in range(N):
            like = count_like(room, r, c, room[r][c])
            total += satisfaction[like]
    return total


# ===output===
classroom = make_classroom()
# print_room(classroom)
ans = cal_satisfaction(classroom)
print(ans)