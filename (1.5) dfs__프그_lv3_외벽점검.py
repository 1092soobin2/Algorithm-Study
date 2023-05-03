 def solution(n: int, weak: list, dist: list):
    answer = 0
    
    if len(weak) == 1:
        return 1
    
    weak += list(map(lambda x: x + n, weak))
    
    def check_wall(weak_list, dist_list):
    
        ret = [20]
        
        def dfs(arr, dist_arr, acc):
            
            # 점검을 마쳤으면 리턴
            if not arr:
                ret[0] = acc
                return
            
            # 더 이상 사람이 없으면 리턴
            if not dist_arr:
                return

            if (acc + 1) >= ret[0]:
                return
            
            now_dist = dist_arr[-1]
            dist_arr = dist_arr[:-1]
            max_delete = 0
            
            for i_start in range(len(arr)):
                
                if (acc + 1) >= ret[0]:
                    break
                # 늘인 리스트에서는 재귀 수행 X
                if arr[i_start] >= n:
                    break
                next_arr = arr[:]
                
                # 점검 가능한 최대 길이 찾기
                i_end = i_start + 1
                while i_end < len(arr) and (arr[i_end] - arr[i_start]) <= now_dist:
                    i_end += 1
                
                if i_end - i_start < max_delete:
                    continue
                else:
                    max_delete = i_end - i_start
                    
                # 점검한 외벽 삭제
                deleted_arr = next_arr[i_start:i_end]
                next_arr = next_arr[:i_start] + next_arr[i_end:]
                for deleted_num in deleted_arr:
                    if deleted_num + n in next_arr:
                        next_arr.remove(deleted_num + n)
                    if deleted_num - n in next_arr:
                        next_arr.remove(deleted_num - n)
                
                # 재귀 고
                # print(f"[{acc+1}] 사람들: {dist_arr}, 삭제됨: {deleted_arr}, 다음 취약벽: {next_arr}")
                dfs(next_arr, dist_arr, acc + 1)
        
        
        dfs(weak_list, dist_list, 0)
        
        if ret[0] == 20:
            return -1
        else:
            return ret[0]
                
        
    answer = check_wall(weak, dist)
    
    return answer
