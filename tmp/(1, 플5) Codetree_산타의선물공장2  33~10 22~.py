# (1, 플5) Codetree_산타의선물공장2  33~10 22~

class Head:
    def __init__(self):
        self.back = None
        self.prev = None
        self.val_set = set()

    def add_val(self, val):
        self.val_set.add(val)

    def set_back(self, node):
        self.back = node

    def set_prev(self, node):
        self.prev = node


class Node:
    def __init__(self, val):
        self.val = val
        self.back = None
        self.prev = None

    def set_back(self, node):
        self.back = node

    def set_prev(self, node):
        self.prev = node


# === input ===
Q = int(input())


# === algorithm ===
g_belt_list = []


# 1. establish
# info: [N, M, B_NUM1, B_NUM2, ..., B_NUMm]
# N belt
# M stuff
def establish(info: list):
    global g_belt_list

    def add_to_belt(node: Node):
        global g_belt_list

        # 처음 삽입되는 노드인 경우
        if not g_belt_list[b_num].back:
            g_belt_list[b_num].set_back(node)
            g_belt_list[b_num].set_prev(node)
            node.set_prev(g_belt_list[b_num])
            node.set_back(g_belt_list[b_num])
        else:
            g_belt_list[b_num].prev.set_back(node)
            g_belt_list[b_num].set_prev(node)
            node.set_prev(g_belt_list[b_num].prev)
            node.set_back(g_belt_list[b_num].set_prev(node))

        g_belt_list[b_num].add_val(node.val)

    n, m = info[0], info[1]
    # 벨트에 헤드 노드 생성 (0번째 : dummy belt)
    g_belt_list = [Head()] + [Head() for _ in range(n)]
    print(len(g_belt_list))

    # 물건 생성
    stuff_id = 1
    for b_num in info[2:]:
        new_node = Node(stuff_id)
        add_to_belt(new_node)
        stuff_id += 1

    print_debug("100(establish) done.")


# 2. move_stuff(m_src: int, m_dst: int) -> int
# m_src 벨트 모든 물건이 m_dst 벨트의 앞으로 옮겨짐
# m_src : 출발 벨트 번호
# m_dst : 도착 벨트 번호
# return : m_dst 벨트의 물건 개수
def move_stuff(m_src: int, m_dst: int) -> int:
    global g_belt_list

    g_belt_list[m_dst] = g_belt_list[m_src] + g_belt_list[m_dst]
    g_belt_list[m_src].clear()

    print_debug(f"200(move) {m_src} -> {m_dst}")

    return len(g_belt_list[m_dst])


# 3. change_stuff(m_src, m_dst) -> int
# m_src와 m_dst 벨트에서 가장 앞의 물건만 교체
# 존재하지 않는 경우 옮기기만 한다.
# return : m_dst 벨트의 물건 개수
def change_stuff(m_src, m_dst) -> int:
    global g_belt_list

    if g_belt_list[m_src] and g_belt_list[m_dst]:
        g_belt_list[m_src][0], g_belt_list[m_dst][0] = g_belt_list[m_dst][0], g_belt_list[m_src][0]
    elif g_belt_list[m_src]:
        g_belt_list[m_dst].append(g_belt_list[m_src][0])
        g_belt_list[m_src] = g_belt_list[m_src][1:]
    elif g_belt_list[m_dst]:
        g_belt_list[m_src].append(g_belt_list[m_dst][0])
        g_belt_list[m_dst] = g_belt_list[m_dst][1:]

    print_debug(f"300(change) {m_src} -> {m_dst}")

    return len(g_belt_list[m_dst])


# 4. divide_stuff(m_src, m_dst) -> int
# m_src 에서 n//2 개 만큼 m_dst 의 앞으로 옮긴다.
# return : m_dst 벨트의 물건 개수
def divide_stuff(m_src, m_dst) -> int:
    global g_belt_list

    if g_belt_list[m_src]:
        g_belt_list[m_dst] = g_belt_list[m_src][:len(g_belt_list[m_src])//2] + g_belt_list[m_dst]
    g_belt_list[m_src] = g_belt_list[m_src][len(g_belt_list[m_src]) // 2:]

    print_debug(f"400(divide) {m_src} -> {m_dst}")

    return len(g_belt_list[m_dst])


# 5. get_stuff_info(p_num: int) -> int
# return: a + 2 * b ( a: 앞 선물 번호, b: 뒤 선물 번호, 없는 경우에는 -1)
def get_stuff_info(p_num: int) -> int:
    for belt in g_belt_list[1:]:
        for i, stuff_id in enumerate(belt):
            if stuff_id == p_num:
                a = belt[i - 1] if i > 0 else -1
                b = belt[i + 1] if i < len(belt) - 1 else -1
                return a + 2*b
    return -3


# 6. get_belt_info(b_num: int) -> int
# return : a + 2*b + 3*c (a: 맨 앞 선물 번호, b : 맨 뒤 선물 번호, 없으면 -1, c: 선물 개수)
def get_belt_info(b_num: int) -> int:
    a, b, c = -1, -1, len(g_belt_list[b_num])
    if c != 0:
        a, b = g_belt_list[b_num][0], g_belt_list[b_num][-1]
    return a + 2*b + 3*c


def solution():

    first_command_line = list(map(int, input().split()))
    establish(first_command_line[1:])

    for _ in range(Q - 1):
        command_line = list(map(int, input().split()))

        # if command_line[0] == 200:
        #     result = move_stuff(*command_line[1:])
        # elif command_line[0] == 300:
        #     result = change_stuff(*command_line[1:])
        # elif command_line[0] == 400:
        #     result = divide_stuff(*command_line[1:])
        # elif command_line[0] == 500:
        #     result = get_stuff_info(*command_line[1:])
        # elif command_line[0] == 600:
        #     result = get_belt_info(*command_line[1:])
        #
        # print(result)


def print_debug(title=""):
    if not DEBUG:
        return

    print("=====================")
    print(title)
    for belt in g_belt_list:
        print(belt.val_set)
    print("=====================")

# === output ===
DEBUG = False
DEBUG = True
solution()
