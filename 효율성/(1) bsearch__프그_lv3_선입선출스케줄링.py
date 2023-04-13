def solution(n, cores):
    answer = 0
    
    num_of_cores = len(cores)
    core_status = [0] * num_of_cores
    
    if n <= num_of_cores:
        answer = n
    else:
        n -= num_of_cores

        min_time = 0
        max_time = 10000*num_of_cores

        # lower bound 찾기
        while min_time < max_time:
            mid_time = (min_time + max_time) // 2
            
            finished_work = 0
            for c in cores:
                finished_work += mid_time // c

            if finished_work >= n:
                max_time = mid_time
            else:
                min_time = mid_time + 1
        
        time = max_time
        # time - 1 시점
        for c in cores:
            n -= (time - 1) // c
        
        # time 시점
        for i, c in enumerate(cores):
            if time % c == 0:
                n -= 1
                if n == 0 :
                    answer = i+1
                
#         core_status = [1] * num_of_cores
#         n -= num_of_cores
#         while n > 0:
            
#             # 시간이 흐른다. 끝난 작업들 빠진다.
#             empty_core_list = []
#             for core_id in range(num_of_cores):
#                 if core_status[core_id] == cores[core_id]:
#                     core_status[core_id] = 0
#                     empty_core_list.append(core_id)
#                 elif core_status[core_id] < cores[core_id]:
#                     core_status[core_id] += 1
#                 else:
#                     print("core_status가 core 성능보다 커짐.") 
#             # print(core_status)
#             # status == 0이면서 앞에 있는 코어에 넣어주기.
#             if empty_core_list:
#                 for core_id in empty_core_list:
#                     if n == 1:
#                         answer = core_id+1
#                     elif n > 1:
#                         core_status[core_id] = 1
#                     else:
#                         print("n이 0보다 작아짐")
#                     n -= 1
                        
            
                
                
        
    return answer