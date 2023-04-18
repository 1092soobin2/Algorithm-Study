def solution(m, n, board):
    answer = 0      # 몇 개의 블록이 지워질지
    
    # return: 지워지는 블록 개수 
    def one_round(arr) -> int:
        ret_num_deleted = 0
        
        def is_4_same(first_loc):
            r, c = first_loc
            is_4_block_same = True
            if arr[r][c] == '0':
                return False
            for dr, dc in [(0, 1), (1, 0), (1, 1)]:
                nr, nc = r+dr, c+dc
                if arr[nr][nc] != arr[r][c]:
                    is_4_block_same = False
                    break
            return is_4_block_same
            
        # 1. soft delete: 삭제 블록들 찾기 -> 2d arr
        deleted = [[False]*n for _ in range(m)]
        for r in range(m-1):
            for c in range(n-1):
                # 안 벗어난다고 가정
                is_same = is_4_same([r, c])
                if is_same:
                    for dr, dc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                        nr, nc = r+dr, c+dc
                        deleted[nr][nc] = True
                        
        # 2. hard delete -> column 기준으로
        new_arr = [['0']*n for _ in range(m)]
        for arr_c in range(n):
            new_r, new_c = m-1, arr_c
            for arr_r in range(m-1, -1, -1):
                if deleted[arr_r][arr_c]:
                    ret_num_deleted += 1
                else:
                    new_arr[new_r][new_c] = arr[arr_r][arr_c]
                    new_r -= 1
        return new_arr, ret_num_deleted
    
    def print_arr(arr):
        for r in range(m):
            print(*arr[r])
        print()
    
    # 문자열을 리스트로 만들어주기
    board = list(map(list, board))
    # 삭제 블록이 0개일 때까지 실행
    while True:
        board, num_of_deleted = one_round(board)  
        answer += num_of_deleted
        if num_of_deleted == 0:
            break
        
    return answer
