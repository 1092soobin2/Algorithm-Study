from collections import deque

def solution(n, results):
    answer = 0
    
    adj_graph = [[None] * (n) for _ in range(n)]
    
    for winner, loser in results:
        adj_graph[winner - 1][loser - 1] = True
        adj_graph[loser - 1][winner - 1] = False
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_graph[i][k] == None:
                    continue
                
                if adj_graph[i][k] == adj_graph[k][j]:
                    adj_graph[i][j] = adj_graph[i][k]
                    adj_graph[j][i] = not adj_graph[i][k]
    
    for i in range(n):
        if None in adj_graph[i][:i] + adj_graph[i][i + 1:]:
            continue
        answer += 1
    
    return answer
