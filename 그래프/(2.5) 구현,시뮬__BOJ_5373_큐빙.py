# (2.5) 구현,시뮬__BOJ_5373_큐빙
# 시뮬 머릿속으로 하다가 잘못함. -> 종이에 그려보기. 직접 시뮬해보기
'''
U-w 윗-흰
D-y 아-노
F앞-빨
B뒷-오렌지
L왼-초
R오-파

ans: 모두 돌린 후 가장 윗 면의 색상
'''
COLOR = ['w', 'y', 'r', 'o', 'g', 'b']


def get_side_id(side: str):
    id_dict = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}
    return id_dict[side]


def print_one_side(cube, side_id):
    s = cube[side_id]
    for i in range(3):
        for j in range(3):
            k = i*3 + j
            print(COLOR[s[k]], end='')
        print()

def print_all_side(cube):
    for i in range(6):
        print_one_side(cube, i)
        print()


def make_cube():
    # UD FB LR
    # U, D, F, B: (0,1,2)는 각각 B, F, U, D에 접한다.
    # L, R: U, D
    return [[i]*9 for i in range(6)]


def rotate_cube(cube: list, side: str, direction: str):
    # 1. adj
    def rotate():
        for i in range(3):
            side_id0, side_id1, side_id2, side_id3 = map(get_side_id, clockwise_side)

            i0, i1, i2, i3 = [indexes[s][i] for s in clockwise_side]
            if direction == '+':
                tmp_value = cube[side_id0][i0]
                cube[side_id0][i0] = cube[side_id3][i3]
                cube[side_id3][i3] = cube[side_id2][i2]
                cube[side_id2][i2] = cube[side_id1][i1]
                cube[side_id1][i1] = tmp_value
            elif direction == '-':
                tmp_value = cube[side_id0][i0]
                cube[side_id0][i0] = cube[side_id1][i1]
                cube[side_id1][i1] = cube[side_id2][i2]
                cube[side_id2][i2] = cube[side_id3][i3]
                cube[side_id3][i3] = tmp_value

    # 2. self
    clockwise = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    counter_clockwise = [2, 5, 8, 1, 4, 7, 0, 3, 6]
    old_side = cube[get_side_id(side)]
    if direction == '+':
        new_side = [old_side[ti] for ti in clockwise]
    elif direction == '-':
        new_side = [old_side[ti] for ti in counter_clockwise]
    cube[get_side_id(side)] = new_side

    # L -> 시계: U-F-D-B, 반시계: U-B-D-F
    indexes = dict()
    clockwise_side = list()
    if side == 'L':
        indexes = {'U': [0, 3, 6], 'F': [0, 3, 6], 'D': [0, 3, 6], 'B': [0, 3, 6]}
        clockwise_side = ['U', 'F', 'D', 'B']
    # R -> 시계: U-B-D-F
    elif side == 'R':
        indexes = {'U': [8, 5, 2], 'F': [8, 5, 2], 'D': [8, 5, 2], 'B': [8, 5, 2]}
        clockwise_side = ['U', 'B', 'D', 'F']
    # U -> 시계: F-L-B-R, 반시계: F-R-B-L
    elif side == 'U':
        indexes = {'F': [2, 1, 0], 'L': [2, 1, 0], 'B': [6, 7, 8], 'R': [6, 7, 8]}
        clockwise_side = ['F', 'L', 'B', 'R']
    # D -> 시계: F-R-B-L
    elif side == 'D':
        indexes = {'F': [6, 7, 8], 'R': [2, 1, 0], 'B': [2, 1, 0], 'L': [6, 7, 8]}
        clockwise_side = ['F', 'R', 'B', 'L']
    # F -> 시계: U-R-D-L, 반시계: U-L-D-R
    elif side == 'F':
        indexes = {'U': [6, 7, 8], 'R': [8, 5, 2], 'D': [2, 1, 0], 'L': [8, 5, 2]}
        clockwise_side = ['U', 'R', 'D', 'L']
    elif side == 'B':
        indexes = {'U': [2, 1, 0], 'R': [0, 3, 6], 'D': [6, 7, 8], 'L': [0, 3, 6]}
        clockwise_side = ['U', 'L', 'D', 'R']

    rotate()


num_of_testcase = int(input())
ans = []
for _ in range(num_of_testcase):
    # ===input===
    n = int(input())        # 큐브를 돌린 횟수
    rotation_order = input().split()

    # ===algorithm===
    cube = make_cube()
    for rotation in rotation_order:
        rotate_cube(cube, rotation[0], rotation[1])
        # print()
        # print(rotation)
        # print_all_side(cube)

    # ===output===
    ans.append(cube[get_side_id('U')])


for up_side in ans:
    for i in range(3):
        for j in range(3):
            k = i*3 + j
            print(COLOR[up_side[k]], end='')
        print()