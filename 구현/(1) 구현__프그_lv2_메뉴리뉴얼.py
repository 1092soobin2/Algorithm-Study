from collections import defaultdict

class Node:
    def __init__(self, node_id, loc):
        self.id = node_id
        self.loc = loc
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        
class bin_tree:
    def __init__(self, num):
        self.root = None
        self.num_node = num
    
    def insert(self, node: Node):
        if not self.root:
            self.root = node
        else:
            self._insert(node)
    
    def _insert(self, node):
        parent_loc = self.root
        insert_loc = parent_loc
        # 자식 노드(insert_loc)가 비어있는 parent_loc 찾기
        while True:
            parent_loc = insert_loc
            if insert_loc.loc[0] > node.loc[0]:
                insert_loc = insert_loc.left
            else:
                insert_loc = insert_loc.right
            if not insert_loc:
                break
        
        node.parent = parent_loc
        if parent_loc.loc[0] > node.loc[0]:
            parent_loc.left = node
        else:
            parent_loc.right = node
    
    def dfs_left(self) -> list:
        ret_list = []
        
        visited = [0] * (self.num_node + 1)
        stack = [self.root]
        visited[self.root.id] = 1
        
        while stack:
            curr = stack.pop()
            ret_list.append(curr.id)
            
            right, left = curr.right, curr.left
            if right and visited[right.id] == 0:
                stack.append(right)
                visited[right.id] = 1
            if left and visited[left.id] == 0:
                stack.append(left)
                visited[left.id] = 1
                
        return ret_list
    
    def dfs_right(self) -> list:
        ret_list = []
        
        visited = [0] * (self.num_node + 1)
        stack = [self.root]
        visited[self.root.id] = 1
        
        while stack:
            curr = stack.pop()
            ret_list.append(curr.id)
            
            right, left = curr.right, curr.left
            if left and visited[left.id] == 0:
                stack.append(left)
                visited[left.id] = 1
            if right and visited[right.id] == 0:
                stack.append(right)
                visited[right.id] = 1
                
        return ret_list
    
def solution(nodeinfo):
    answer = []
    
    # front -> left-first dfs
    # back -> right-first dfs [::-1]
    
    # y 기준 딕셔너리
    nodeinfo = list(map(lambda x: (x[0]+1, x[1]), enumerate(nodeinfo)))
    y_dict = defaultdict(list)
    for info in nodeinfo:
        y_dict[info[1][1]].append(info)
    # x 기준 오름차순 정렬
    for y in y_dict:
        y_dict[y].sort(key=lambda x: x[1][0])
    
    binary_tree = bin_tree(len(nodeinfo))
    
    y_list = sorted(y_dict.keys(), key=lambda x: -x)
    for y in y_list:
        for info in y_dict[y]:
            node = Node(node_id=info[0], loc=info[1])
            binary_tree.insert(node)
    
    answer.append(binary_tree.dfs_left())
    answer.append(binary_tree.dfs_right()[::-1])
    return answer
