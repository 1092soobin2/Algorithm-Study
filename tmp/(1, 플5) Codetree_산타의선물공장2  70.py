# (1, 플5) Codetree_산타의선물공장2  70

class Head:
    def __init__(self):
        self.next = None
        self.prev = None
        self.val_set = set()

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node

    def add_node(self, node):
        # set에 값 넣어주기
        self.val_set.add(node.val)

        # 연결 리스트에 노드 추가
        if self.next:
            self.next.set_prev(node)
            node.set_next(self.next)
            self.set_next(node)
            node.set_prev(self)
        else:
            self.set_prev(node)
            node.set_next(self)
            self.set_next(node)
            node.set_prev(self)

    def pop_node(self):
        node = self.next
        print(node.val)
        self.val_set.remove(node.val)

        if node.next != self:
            self.set_next(node.next)
            node.next.set_prev(self)
        else:
            self.set_next(None)
            self.set_prev(None)

        node.set_next(None)
        node.set_prev(None)

        return node

    def move_all_node(self, src_head):
        if not src_head.next:
            return

        if self.next:
            self.next.set_prev(src_head.prev)       # 현재 첫 노드의 앞에 연결
            src_head.prev.set_next(self.next)
            self.set_next(src_head.next)            # 첫 노드로 연결
            src_head.next.set_prev(self)
        else:
            self.set_prev(src_head.prev)
            src_head.prev.set_next(self)
            self.set_next(src_head.next)
            src_head.next.set_prev(self)

        src_head.set_next(None)
        src_head.set_prev(None)
        self.val_set |= src_head.val_set
        src_head.val_set = set()

    def change_one_node(self, src_head):
        if self.next and src_head.next:     # 둘 다 있는 경우
            src_node_1 = src_head.pop_node()
            dst_node_1 = self.pop_node()
            src_head.add_node(dst_node_1)
            self.add_node(src_node_1)
        elif self.next:                         # dst에만 있는 경우
            dst_node_1 = self.pop_node()        # dst 에서 삭제
            src_head.add_node(dst_node_1)       # src에 추가
        elif src_head.next:
            src_node_1 = src_head.pop_node()
            self.add_node(src_node_1)

    def divide_node(self, src_head):
        num_of_src = len(src_head)
        for _ in range(num_of_src // 2):
            node = src_head.pop_node()
            self.add_node(node)

    def __len__(self):
        return len(self.val_set)

    def get_first_node(self):
        return self.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def set_next(self, node):
        self.next = node

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

    n, m = info[0], info[1]
    # 벨트에 헤드 노드 생성 (0번째 : dummy belt)
    g_belt_list = [Head()] + [Head() for _ in range(n)]
    print(len(g_belt_list))

    # 물건 생성
    stuff_id = 1
    for b_num in info[2:]:
        new_node = Node(stuff_id)
        g_belt_list[b_num].add_node(new_node)
        stuff_id += 1

    print_debug("100(establish) done.")


# 2. move_stuff(m_src: int, m_dst: int) -> int
# m_src 벨트 모든 물건이 m_dst 벨트의 앞으로 옮겨짐
# m_src : 출발 벨트 번호
# m_dst : 도착 벨트 번호
# return : m_dst 벨트의 물건 개수
def move_stuff(m_src: int, m_dst: int) -> int:
    global g_belt_list
    
    g_belt_list[m_dst].move_all_node(g_belt_list[m_src])

    print_debug(f"200(move) {m_src} -> {m_dst}")
    return len(g_belt_list[m_dst])


# 3. change_stuff(m_src, m_dst) -> int
# m_src와 m_dst 벨트에서 가장 앞의 물건만 교체
# 존재하지 않는 경우 옮기기만 한다.
# return : m_dst 벨트의 물건 개수
def change_stuff(m_src, m_dst) -> int:
    global g_belt_list

    g_belt_list[m_dst].change_one_node(g_belt_list[m_src])

    print_debug(f"300(change) {m_src} -> {m_dst}")
    return len(g_belt_list[m_dst])


# 4. divide_stuff(m_src, m_dst) -> int
# m_src 에서 n//2 개 만큼 m_dst 의 앞으로 옮긴다.
# return : m_dst 벨트의 물건 개수
def divide_stuff(m_src, m_dst) -> int:
    global g_belt_list

    g_belt_list[m_dst].divide_node(g_belt_list[m_src])

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

        if command_line[0] == 200:
            result = move_stuff(*command_line[1:])
        elif command_line[0] == 300:
            result = change_stuff(*command_line[1:])
        elif command_line[0] == 400:
            result = divide_stuff(*command_line[1:])
        # elif command_line[0] == 500:
        #     result = get_stuff_info(*command_line[1:])
        # elif command_line[0] == 600:
        #     result = get_belt_info(*command_line[1:])

        print(result)


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
