def solution(board):
    answer = 0
    
    EMPTY = 0
    WALL = 1
    N = len(board)
    visited = [[[1e9]*4 for _ in range(N)] for _ in range(N)]
    
    direction_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def dfs(curr_r, curr_c, curr_d, acc):
        # 도착하면 돌아가기
        if curr_r == N-1 and curr_c == N-1:
            return
        
        for i in range(4):
            next_d = (curr_d + i) % 4
            dr, dc = direction_list[next_d]
            nr, nc = curr_r+dr, curr_c+dc
            # 격자 안이면서, 빈 칸이면 진행
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == EMPTY:
                next_acc = acc
                if curr_d == next_d:
                    next_acc = acc+100
                else:
                    next_acc = acc+600
                # 다음 acc이 더 작으면 진행
                if visited[nr][nc][next_d] > next_acc:
                    visited[nr][nc][next_d] = next_acc
                    board[curr_r][curr_c] = WALL
                    dfs(nr, nc, next_d, next_acc)  
                    board[curr_r][curr_c] = EMPTY
                    
    
    dfs(0, 0, 2, 0)
    dfs(0, 0, 3, 0)
    # for i in range(N-1):
        # print(*visited[i])
    answer = min(visited[N-1][N-1])
    
    return answer
