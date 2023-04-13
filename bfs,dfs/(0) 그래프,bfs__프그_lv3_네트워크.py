def solution(n, computers):
    answer = 0
    
    visited = [False]*n
    
    def bfs(start):
        
        will_visited_stack = [start]
        visited[start] = True
        
        while will_visited_stack:
            curr_computer = will_visited_stack.pop(0)
            
            for next_computer in range(n):
                if next_computer == curr_computer:
                    continue
                if visited[next_computer]:
                    continue
                if computers[curr_computer][next_computer] == 1:
                    will_visited_stack.append(next_computer)
                    visited[next_computer] = True
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer
