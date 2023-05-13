# __Codetree_산타의선물공장 2.5h

# stuff constants
ID = 0
DELETED = 1

# belt constants
BREAKDOWN = 0
START_POINT = 1
STUFF_DELETED = 2
STUFF_DICT = 3

# TODO: stuff 접근 전에 DELETED 확인
# TODO: belt 접근 전에 BREAKDOWN 확인
# TODO: belt[STUFF_LIST] empty인지 확인

len_of_belts = 0
# belt[0]: [N/A, start, [], {}]
# belt[1]: [Availabe, start=0, [(id, deleted),..], {id: w, id2:w2, ...}]
belts = [[True, 0, [], dict()]]

# ===input===
num_of_commands = int(input())
# command 1
establish_arguments = list(map(int, input().split()))
# command 2 - command N
commands = [list(map(int, input().split())) for _ in range(num_of_commands-1)]


# ===algorithm===
# 1. 공장 설립
def establish_factory(arg):
    global belts, len_of_belts
    n, m, = arg[0], arg[1]

    # 1) m belt (1, 2, ...m번 벨트)
    # 2) n/m 물건들
    len_of_belts = m
    stride = int(n/m)
    for stuff_index in range(0, n, stride):
        start_i = 2 + stuff_index
        end_i = start_i + stride

        stuff_list = list(map(list, zip(arg[start_i:end_i], [False] * stride)))
        stuff_dict = dict(zip(arg[start_i:end_i], arg[start_i + n: end_i + n]))

        belts.append([False, 0, stuff_list, stuff_dict])


# 2. 물건 하차 (w_max)
def take_down_stuffs(w_max) -> int:
    # 1) w <= w_max -> 하차
    # 2) w > w_max -> 벨트의 맨 뒤로
    # 3) 출력 sum(하차된 상 무게)
    total_w = 0

    for belt in belts:
        if belt[BREAKDOWN]:
            continue
        # 시작점 부터 not deleted stuff를 찾기
        stuff_i = belt[START_POINT]
        stuff_deleted = belt[STUFF_DELETED]
        stuff_weight_dict = belt[STUFF_DICT]
        len_of_stuffs = len(stuff_deleted)
        while stuff_i < len_of_stuffs:
            stuff = stuff_deleted[stuff_i]
            if not stuff[DELETED]:
                if stuff_weight_dict[stuff[ID]] <= w_max:
                    total_w += stuff_weight_dict[stuff[ID]]
                else:
                    # 맨 뒤로
                    new_stuff = stuff[:]
                    stuff_deleted.append(new_stuff)
                # 맨 앞 물 건 삭제
                belt[START_POINT] += 1
                stuff[DELETED] = True
                break
            stuff_i += 1
    return total_w


# 3. 물건 제거 (r_id)
def remove_stuff(r_id):
    # 1) 제거하고 벨트를 채움
    # 2) 출력 r_id (if r_id in belts else -1)
    for belt in belts:
        if belt[BREAKDOWN]:
            continue
        # belt에 id가 있는지 확인, 삭제되지 않았는지 확인
        if r_id in belt[STUFF_DICT]:
            # 시작점 부터 not deleted stuff를 찾기
            stuff_i = belt[START_POINT]
            stuff_deleted = belt[STUFF_DELETED]
            len_of_stuffs = len(stuff_deleted)
            while stuff_i < len_of_stuffs:
                stuff = stuff_deleted[stuff_i]
                if stuff[ID] == r_id:
                    if not stuff[DELETED]:
                        stuff[DELETED] = True
                        return r_id
                    else:
                        return -1
                stuff_i += 1
            break

    return -1


# 4. 물건 확인 (f_id)
def find_stuff(f_id):
    # 1) f_id X -> print(-1)
    # 2) f_id O -> print(belt_id), f_id 뒤의 모든 상자를 앞으로 가져온다.
    for b_index, belt in enumerate(belts):
        if belt[BREAKDOWN]:
            continue
        # belt에 id가 있는지 확인, 삭제되지 않았는지 확인
        if f_id in belt[STUFF_DICT]:
            # 시작점 부터 not deleted stuff를 찾기
            stuff_i = belt[START_POINT]
            stuff_deleted = belt[STUFF_DELETED]
            len_of_stuffs = len(stuff_deleted)
            while stuff_i < len_of_stuffs:
                stuff = stuff_deleted[stuff_i]
                if stuff[ID] == f_id:
                    if not stuff[DELETED]:
                        # TODO: 0, 1, 2
                        new_stuff_deleted = stuff_deleted[stuff_i:] + stuff_deleted[belt[START_POINT]:stuff_i]
                        belt[STUFF_DELETED] = new_stuff_deleted
                        belt[START_POINT] = 0
                        return b_index
                    break
                stuff_i += 1
            break

    return -1


# 5. 벨트 고장 (b_num) TODO belt_breakdown update
def breakdown_belt(b_num):
    # 1) b_num belt 고장 O -> print(-1)
    # 2) 고장 X -> print(b_num)
    # 3) b_num+1, b_num-1 까지 차례로 확인
    # 4) 최초의 고장 X 벨트로 모든 상자를 옮김

    if b_num > len_of_belts:
        return -1

    if belts[b_num][BREAKDOWN]:
        return -1
    else:
        belts[b_num][BREAKDOWN] = True

        for added_index in range(1, len_of_belts):
            belt_index = b_num + added_index
            if belt_index > len_of_belts:
                belt_index -= len_of_belts
            if not belts[belt_index][BREAKDOWN]:
                abnormal = belts[b_num]
                normal = belts[belt_index]
                normal[STUFF_DELETED] += abnormal[STUFF_DELETED]
                normal[STUFF_DICT] = dict(normal[STUFF_DICT].items()|abnormal[STUFF_DICT].items())
                return b_num

    return -1


def print_belt(title=""):
    global belts
    print(title)
    for belt in belts:
        if belt[BREAKDOWN]:
            continue
        print(list(filter(lambda x: not x[1], belt[STUFF_DELETED])))


# ===output===
establish_factory(establish_arguments[1:])
# print_belt()
for command, arg in commands:
    # print("\n\n\n")
    ret_val = 0
    if command == 200:
        ret_val = take_down_stuffs(arg)
    elif command == 300:
        ret_val = remove_stuff(arg)
    elif command == 400:
        ret_val = find_stuff(arg)
    elif command == 500:
        ret_val = breakdown_belt(arg)
    else:
        exit()
    # print_belt(f" command, arg: {command ,arg}")
    print(ret_val)


