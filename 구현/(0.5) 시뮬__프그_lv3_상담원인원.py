# 16:00~

# n mento [type]
# k type
# 1:1 상담
# 1. 상담 유형의 멘토 중 상담 중이 아닌 멘토와 상담 시작
# 2. 모두 상담 중이라면 기다림 (기다린 시간 = (상담 시작 시간) - (상담 요청 시간))
# 3. 상담이 끝났을 때, 기다리는 참가자가 있으면 즉시 상담 시작, 선착순

# answer: 기다린 시간의 합이 최소가 되는 멘토 인원을 정한다
import heapq


answer = 1e9
mento_last_time_list = []


def check_waiting_time(reqs) -> int:
    global mento_last_time_list
    
    # print(mento_last_time_list)
    waiting_time = 0
    
    for req_time, duration, consulting_type in reqs:
        
        cst_type = consulting_type - 1
        
        start_time = heapq.heappop(mento_last_time_list[cst_type])
        waiting_time += start_time - req_time if start_time > req_time else 0
        heapq.heappush(mento_last_time_list[cst_type], max(start_time, req_time) + duration)
        # print(mento_last_time_list)
        if answer < waiting_time:
            return 1e9
    # print("=============")
    return waiting_time


def dfs(rest_type, rest_mento, acc_mento, reqs):
    global mento_last_time_list, answer
    
    if rest_type == 1 or rest_mento == 0:
        acc_mento[-1] += rest_mento
        mento_last_time_list = [[0] * mento for mento in acc_mento]
        answer = min(answer, check_waiting_time(reqs))
        return
    
    for mento in range(rest_mento + 1):
        new_acc = acc_mento[:]
        new_acc[-rest_type] += mento
        dfs(rest_type - 1, rest_mento - mento, new_acc, reqs)

    
def solution(k, n, reqs):
    
    dfs(k, n - k, [1]*k, reqs)
    return answer
