import sys
sys.setrecursionlimit(200000)
class Node:
    def __init__(self):
        self.profit = 0
        self.parent = None
        self.child_list = list()
    
    def set_parent(self, parent):
        self.parent = parent
    
    def add_child (self, child_node):
        self.child_list.append(child_node)
    
    def add_profit(self, money):
        self.profit += money
    

def give_profit(curr:Node, profit):
    if curr.parent:
        partial_profit = int(profit * 0.1)
        if partial_profit == 0:
            return
        curr.profit -= partial_profit
        curr.parent.add_profit(partial_profit)
        give_profit(curr.parent, partial_profit)


def solution(enroll, referral, seller, amount):
    answer = []
    
    # 각 멤버에게 id 부여
    num_enrolled = len(enroll)
    id_dict = dict()
    for i in range(num_enrolled):
        id_dict[enroll[i]] = i
    
    # tree 생성
    node_list = [Node() for _ in range(num_enrolled)]
    root = Node()
    for child_id, parent in enumerate(referral):
        # parent is root
        if parent == "-":
            root.add_child(node_list[child_id])
            node_list[child_id].set_parent(root)
        # parent is not root
        else:
            node_list[id_dict[parent]].add_child(node_list[child_id])
            node_list[child_id].set_parent(node_list[id_dict[parent]])
    
    for s, a in zip(seller, amount):
        node_list[id_dict[s]].add_profit(a * 100)
        give_profit(node_list[id_dict[s]], a * 100)
        
    
    for n in node_list:
        answer.append(n.profit)
        
    return answer
