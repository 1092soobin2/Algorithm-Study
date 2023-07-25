# (1, 골2) Codetree_윷놀이사기단


# 시작칸 말 4개

# 화살표를 따라서만 이동
# 파란 칸 시작 -> 빨간색 방향



# 칸에 있는 점수를 받

import copy

# === input ===
move_list = list(map(int, input().split()))


# === algorithm ===
class Node:
    def __init__(self, score):
        self.score = score
        self.black = None
        self.red = None

    def set_black(self, black):
        self.black = black

    def set_red(self, red):
        self.red = red


class Board:
    def __init__(self):
        self.start = Node(0)
        self.arrival = Node(1)

        # 2, 4, ..., 40 까지 만들기
        ten, twenty, thirty, forty = None, None, None, None

        prev_node = self.start  # 다음 노드와 연결하기 위해 저장하기
        for i in range(2, 41, 2):
            new_node = Node(i)  # 노드 생성
            prev_node.black = new_node  # 앞 노드와 연결

            prev_node = new_node  # 앞 노드 현 노드로 업데이트

            if i == 10:  # 새로운 길을 만들기 위해 저장해 두기
                ten = new_node
            elif i == 20:
                twenty = new_node
            elif i == 30:
                thirty = new_node
            elif i == 40:
                forty = new_node

        # arrival 과 연결하기
        prev_node.black = self.arrival

        # 22, 24, 25, 30, 35, 40
        twenty_five = None

        new_node = Node(22)
        twenty.red = new_node
        prev_node = new_node
        for i in [24, 25, 30, 35, 40]:
            new_node = Node(i)
            prev_node.black = new_node

            prev_node = new_node

            if i == 25:
                twenty_five = new_node
        prev_node.black = forty

        # 13, 16, 19
        new_node = Node(13)
        ten.red = new_node
        prev_node = new_node
        for i in [16, 19]:
            new_node = Node(i)
            prev_node.black = new_node

            prev_node = new_node
        prev_node.black = twenty_five

        # 28, 27, 26
        new_node = Node(28)
        thirty.red = new_node
        prev_node = new_node
        for i in [27, 26]:
            new_node = Node(i)
            prev_node.black = new_node

            prev_node = new_node
        prev_node.black = twenty_five

    # 인자: 위치, 이동 횟수
    def move(self, location: Node, move_num: int):
        node = location
        # 첫 이동
        node = location.red if not location.red else location.black
        # 두 번째 이동
        while move_num > 0:
            move_num -= 1
            node = location.black

        return node


board = Board()


def dfs(loc_list, i, acc):
    # 10개 턴
    # 도착하지 않은 말을 원하는 이동횟수만큼 이동
    if i == 10:
        return acc

    # 4말을 한 번씩 움직이기
    score = [0]*4
    for horse in range(4):
        # 도착 위치에 다른 말이 이미 있으면 -> 이동 불가능
        if loc_list[horse] == board.arrival:
            continue
        new_loc_list = copy.deepcopy(loc_list)
        new_loc_list[horse] = board.move(loc_list[horse], move_list[i])
        score[horse] = dfs(new_loc_list, i + 1, acc + new_loc_list[horse].score)

    print(f"{i}-th turn, score:{score}")
    return max(score)


# === output ===
print(dfs([board.start, board.start, board.start, board.start], 0, 0))

