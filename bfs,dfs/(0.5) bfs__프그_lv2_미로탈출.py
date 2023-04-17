from collections import deque

def solution(maps):
    answer = 0
    
    WALL = 'X'
    
    len_row = len(maps)
    len_col = len(maps[0])
    
    # 시작, 레버, 출구 구하기
    src = [0, 0]
    dst1 = [0, 0]
    dst2 = [0, 0]
    for r in range(len_row):
        for c in range(len_col):
            if maps[r][c] == 'S':
                src = [r, c]
            elif maps[r][c] == 'L':
                dst1 = [r, c]
            elif maps[r][c] == 'E':
                dst2 = [r, c]
                
    def bfs(start, dst) -> int:
        stack = deque()
        dist = [ [-1]*len_col for _ in range(len_row)]
        
        # start
        stack.append(start)
        dist[start[0]][start[1]] = 0
        
        while stack:
            r, c = stack.popleft()
            d = dist[r][c]
            
            if r == dst[0] and c == dst[1]:
                return d
                
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < len_row and 0 <= nc < len_col:
                    if maps[nr][nc] != WALL and dist[nr][nc] == -1:
                        dist[nr][nc] = d+1
                        stack.append([nr, nc])
        
        # dst에 도착할 수 없으면 -1 리턴
        return -1
    
    # path1 계산
    path1 = bfs(src, dst1)
    if path1 == -1:
        return -1
    
    answer += path1
    path2 = bfs(dst1, dst2)
    if path2 == -1:
        return -1
    answer += path2
    return answer
