
def solution(n, edge):
    answer = 0
    
    # 0. edge 등록
    adj_list = [list() for _ in range(n+1)]
    for node1, node2 in edge:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    
    # 1. 각 노드들 과의 거리 구하기 bfs
    distances = []
    
    def bfs(start_node, edges) -> list:
        ret_dists = []
        
        will_visited_stack = []
        dist = [-1]*(n+1)
        
        # 시작 노드 1
        will_visited_stack.append(start_node)
        dist[start_node] = 0
        
        while will_visited_stack:
            curr_node = will_visited_stack.pop(0)
            curr_dist = dist[curr_node]
            
            for next_node in edges[curr_node]:
                if dist[next_node] == -1:
                    will_visited_stack.append(next_node)
                    dist[next_node] = curr_dist+1
                    ret_dists.append(curr_dist+1)
        return ret_dists
        
    distances = bfs(1, adj_list)
    
    # 2. 가장 먼 거리 구하기
    # 3. 가장 먼 노드들 구하기
    answer = distances.count(distances[-1])
    
    return answer