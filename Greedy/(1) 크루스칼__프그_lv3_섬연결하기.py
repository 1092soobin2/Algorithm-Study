def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2])
    parent = list(range(n))
    
    def find_parent(node): 
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]
    
    for v1, v2, cost in costs:
        root1 = find_parent(v1)
        root2 = find_parent(v2)
        
        if root1 != root2:
            new_root = min(root1, root2)
            parent[root1] = new_root
            parent[root2] = new_root
            answer += cost
    
    return answer
