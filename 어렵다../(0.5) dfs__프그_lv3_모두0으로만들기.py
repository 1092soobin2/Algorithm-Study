import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    answer = 0
    
    # 각 점에 w
    # all w -> 0
    
    num_of_nodes = 0
    sum_of_nodes = 0
    for num in a:
        sum_of_nodes += num
        num_of_nodes += 1
    
    # 합이 0이 아니면 모두 0으로 만들 수 없음
    if sum_of_nodes != 0:
        return -1
    
    adj_list = [list() for _ in range(num_of_nodes)]
    for v1, v2 in edges:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    
    answers = [0]
    visited = [False]*num_of_nodes
    
    def dfs(curr):
        visited[curr] = True
    
        for child in adj_list[curr]:
            # 부모 노드이면 숫자를 모으지 X
            if not visited[child]:
                a[curr] += dfs(child)
        
        answers[0] += abs(a[curr])
        return a[curr]
            
    dfs(0)  
    answer = answers[0]
    
    return answer
