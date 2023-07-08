# (1, 플4) Codetree_산타의선물공장 15 + 45~


# === input ===
Q = int(input())
command_list = [list(map(int, input().split())) for _ in range(Q)]


# === algorithm ===
g_stuff_dict = dict()     # id: [w, belt_number, prev_id, next_id]
g_belt_list = []        # [고장여부, 맨 앞 stuff_id, 맨뒤]
BROKEN, HEAD, TAIL = 0, 1, 2
WEIGHT, B_NUM, PRV, NXT = 0, 1, 2, 3


# 1. 공장 설립
def establish(info):
    global g_belt_list, g_stuff_dict

    # m개 밸트에 n개 물건
    n, m = info[0], info[1]
    g_belt_list = [[False, 0, 0] for _ in range(m + 1)]

    # 물건 [id, w] -> dict
    for b_num in range(1, m+1):
        b_idx = 2 + (n // m) * (b_num - 1)

        # 벨트 리스트
        g_belt_list[b_num][HEAD] = info[b_idx]
        g_belt_list[b_num][TAIL] = info[b_idx + n // m - 1]

        # 선물 딕셔너리
        g_stuff_dict[info[b_idx]] = [info[b_idx + n], b_num, 0, info[b_idx + 1]]
        for idx in range(1, n // m - 1):
            stuff_idx = b_idx + idx
            w_idx = stuff_idx + n
            g_stuff_dict[info[stuff_idx]] = [info[w_idx], b_num, info[stuff_idx - 1], info[stuff_idx + 1]]

        last_idx = b_idx + n // m - 1
        g_stuff_dict[info[last_idx]] = [info[last_idx + n], b_num, info[last_idx - 1], 0]

    print_debug("establish() done.")


# def pop(stuff_id):
#     global g_stuff_dict
#
#     stuff = g_stuff_dict[stuff_id]
#
#     # head이면
#     if stuff[PRV] == 0:
#         s
#
# def push():

# 2. 물건 하차
# return : 하자된 물건 무게 총합
def get_off_stuff(w_max):
    global g_belt_list

    total_w = 0

    for belt_info in g_belt_list:
        if belt_info[HEAD] == 0:
            continue

        head_id = belt_info[HEAD]
        head_stuff = g_stuff_dict[head_id]

        # 맨 앞에서 제거
        belt_info[HEAD] = head_stuff[NXT]
        g_stuff_dict[head_stuff[NXT]][PRV] = 0
        head_stuff[NXT] = 0

        # 각 벨트의 (맨 앞 선물 w) <= w_max -> 하차
        if head_stuff[WEIGHT] <= w_max:
            del g_stuff_dict[head_id]
            total_w += head_stuff[WEIGHT]
        # 그렇지 않으면 맨 뒤로 보냄
        else:
            g_stuff_dict[belt_info[TAIL]][NXT] = head_id
            head_stuff[PRV] = belt_info[TAIL]
            belt_info[TAIL] = head_id

    print_debug(f"200: get_off({w_max}) done.")
    
    return total_w


# 3. 물건 제거
def remove_stuff(r_id):
    global g_belt_list, g_stuff_dict

    # 물건 X -> -1
    if r_id not in g_stuff_dict:
        return -1

    # 물건 O -> 제거하기
    stuff = g_stuff_dict[r_id]

    # head 이면 head 갱신
    if stuff[PRV] == 0:
        g_belt_list[stuff[B_NUM]][HEAD] = stuff[NXT]
    else:
        g_stuff_dict[stuff[PRV]][NXT] = stuff[NXT]

    if stuff[NXT] == 0:
        g_belt_list[stuff[B_NUM]][TAIL] = stuff[PRV]
    else:
        g_stuff_dict[stuff[NXT]][PRV] = stuff[PRV]

    del g_stuff_dict[r_id]

    print_debug(f"300: remove_stuff({r_id})")

    return r_id


# 4. 물건 확인
def access_stuff(f_id):
    global g_belt_list, g_stuff_dict

    # 물건 X -> -1
    if f_id not in g_stuff_dict:
        return -1

    # 물건 O -> 물건 + 뒷 물건들 모두 앞으로 가져오기
    stuff = g_stuff_dict[f_id]
    # f_id가 head인 경우
    if stuff[PRV] == 0:
        pass
    # f_id가 tail인 경우 (head가 아님)
    elif stuff[NXT] == 0:
        head_id = g_belt_list[stuff[B_NUM]][HEAD]

        # tail 갱신
        g_belt_list[stuff[B_NUM]][TAIL] = stuff[PRV]
        g_stuff_dict[stuff[PRV]][NXT] = 0

        # head 갱신 (하나만 앞으로 가져오기)
        g_stuff_dict[head_id][PRV] = f_id
        stuff[NXT] = head_id

        g_belt_list[stuff[B_NUM]][HEAD] = f_id
        stuff[PRV] = 0
    else:
        tail_id = g_belt_list[stuff[B_NUM]][TAIL]
        head_id = g_belt_list[stuff[B_NUM]][HEAD]

        # head 갱신 (모두 앞으로 가져오기)
        g_stuff_dict[head_id][PRV] = tail_id
        g_stuff_dict[tail_id][NXT] = head_id

        g_belt_list[stuff[B_NUM]][HEAD] = f_id
        stuff[PRV] = 0

        # tail 갱신
        g_belt_list[stuff[B_NUM]][TAIL] = stuff[PRV]
        g_stuff_dict[stuff[PRV]][NXT] = 0

    print_debug(f"400 access_stuff({f_id})")
    return g_stuff_dict[f_id][B_NUM]


# 5. 벨트 고장
def break_belt(b_num):
    global g_belt_list, g_stuff_dict

    # 이미 망가져 있었다면 -1
    if g_belt_list[b_num][BROKEN]:
        return -1

    g_belt_list[b_num][BROKEN] = True

    if g_belt_list[b_num][HEAD] != 0:
        # 오른쪽 벨트부터, 고장 X 최초 벨트로 모든 물건 옮김
        for belt_info in g_belt_list[b_num:]:
            if not belt_info[BROKEN]:
                tail_id = belt_info[TAIL]
                head_id = g_belt_list[b_num][HEAD]

                g_stuff_dict[tail_id][NXT] = head_id
                g_stuff_dict[head_id][PRV] = tail_id

                belt_info[TAIL] = g_belt_list[b_num][TAIL]

    print_debug("500")

    return b_num

# 정상 처리 -> b_num

def solution():

    establish(command_list[0][1:])

    for command in command_list[1:]:
        if command[0] == 200:
            result = get_off_stuff(command[1])
        elif command[0] == 300:
            result = remove_stuff(command[1])
        elif command[0] == 400:
            result = access_stuff(command[1])
        elif command[0] == 500:
            result = break_belt(command[1])
        else:
            result = 0

        print(result)


def print_debug(title=""):
    if not DEBUG:
        return

    print("====================================")
    print(title)
    for belt_info in g_belt_list:
        print(belt_info[BROKEN], end="\t")
        curr_id = belt_info[HEAD]
        while curr_id != 0:
            print(f"{curr_id:4}", end="")
            curr_id = g_stuff_dict[curr_id][NXT]
        print()
    print("====================================")


# === output ===

DEBUG = False
# DEBUG = True

solution()
