# (1.5) 구현__BOJ_20057_마법사상어와파이어볼
# 반복문에서 객체 사용 시 deepcopy고려. 파이썬은 대부분 객체 참조임
'''
NxN board
M fireball
r, c, m(mass), s(speed), d    1<=r<=N

1. 모든 파이어볼이 d 방향으로 s만큼 이동한다.
2. 2개 이상의 파이어볼이 있는 칸
    1. 하나로 합쳐진다.
    2. 4개로 나누어진다.
        - mass: sum(m) // 5
        - speed: sum(s) // num(fierball)
        - direction: 모두홀수||모두짝수 -> 0, 2, 4, 6 /  그렇지 않으면 1, 3, 5, 7
    3. 질량이 0이면 소멸한다.
3. K번 반복 후 남은 sum(m)
'''

import time
import copy
start_time = time.time()
# ===input===
N, M, K = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(M)]


# ===algorithm===
def make_fireball_dict(fireballs_list):
    new_dict = dict()
    for fireball in fireballs_list:
        new_dict[(fireball[0]-1, fireball[1]-1)] = [fireball[2:]]
        # 위치 업데이트: dict에서 삭제, 다시 넣어주기
    return new_dict


# def move_fireball(from_loc: tuple, to_loc: tuple) :
#     fireballs_dict[from_loc]


def move_fireballs(fireball_dict):
    def add_to_fireball_dict(key, val):
        if key in fireball_dict:
            fireball_dict[key].append(val)
        else:
            fireball_dict[key] = [val]

    def remove_from_fireball_dict(key, val):
        fireball_dict[key].remove(val)
        if not fireball_dict[key]:
            del (fireball_dict[key])

    direction_list = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]

    # 파이어볼 이동
    old_dict = copy.deepcopy(fireball_dict)
    for from_loc, fireballs in old_dict.items():
        if len(fireballs) == 4:
            pass
        for fireball in fireballs:
            # 다음 위치
            r, c = from_loc
            dr, dc = direction_list[fireball[2]]
            s = fireball[1]
            to_loc = ((r+dr*s) % N, (c+dc*s) % N)
            # 파이어볼 위치 업데이트
            add_to_fireball_dict(to_loc, fireball)
            remove_from_fireball_dict(from_loc, fireball)


def divide_fireballs(fireball_dict):
    old_dict = copy.deepcopy(fireball_dict)
    for fire_loc, fireballs in old_dict.items():
        num_of_fireballs = len(fireballs)
        if num_of_fireballs > 1:
            all_directions = list()
            total_mass = 0
            total_speed = 0
            for m, s, d in fireballs:
                total_mass += m
                total_speed += s
                all_directions.append(d % 2)
            mass = total_mass // 5
            speed = total_speed // num_of_fireballs
            same_flag = True
            for i in range(1, num_of_fireballs):
                if all_directions[i] != all_directions[i-1]:
                    same_flag = False
                    break
            # 모두 삭제 후 새로운 4개 추가
            if mass == 0:
                del(fireball_dict[fire_loc])
            else:
                if same_flag:
                    fireball_dict[fire_loc] = [(mass, speed, 2*i) for i in range(4)]
                else:
                    fireball_dict[fire_loc] = [(mass, speed, 2*i + 1) for i in range(4)]


def sum_mass(fireball_dict) -> int:
    total_mass = 0
    for fireballs in fireball_dict.values():
        for m, _, _ in fireballs:
            total_mass += m

    return total_mass


# ===output===
fireball_dictionary = make_fireball_dict(input_list)
for _ in range(K):
    move_fireballs(fireball_dictionary)
    divide_fireballs(fireball_dictionary)
print(sum_mass(fireball_dictionary))

end_time = time.time()
# print("time:", end_time-start_time)