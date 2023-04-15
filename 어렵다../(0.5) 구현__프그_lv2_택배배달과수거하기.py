import sys
sys.setrecursionlimit(10000)

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    # n x m maze
    maze = [[0]*(n+1) for _ in range(m+1)]
    direction_list = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    
    def get_direction(direction):
        d_dict = {(1, 0): "d", (0, -1): "l", (0, 1): "r", (-1, 0): "u"}
        return d_dict[direction]
    
    # (x, y) start
    # (r, c) end

    shortest_dist = abs(r-x) + abs(c-y)
    if shortest_dist > k or (k-shortest_dist) % 2 != 0:
        answer = "impossible"
    else:
        answers = []
        def dfs(curr_r, curr_c, path):
            if answers:
                return
            
            if len(path) == k:
                if curr_r == r and curr_c == c:
                    answers.append(path)
                return
            
            curr_dist =  abs(r-curr_r) + abs(c-curr_c)
            if curr_dist > k - len(path):
                return

            for curr_d in direction_list:
                dr, dc = curr_d
                next_r, next_c = curr_r+dr, curr_c+dc
                if 1 <= next_r <= n and 1 <= next_c <= m:
                    dfs(next_r, next_c, path + [get_direction(curr_d)])


        dfs(x, y, [])
        if answers:
            answer = ''.join(answers[0])
        else:
            answer = "impossible"
    return answer
