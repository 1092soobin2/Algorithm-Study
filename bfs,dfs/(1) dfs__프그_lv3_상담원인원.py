# 21:40 ~

# 멘토 n명
# 1~k번으로 분류되는 상담 유형 (talk_type)
# 각 멘토는 k개의 상담 유형 중 하나만 담당 (n >= k)
# req: [REQ_TIME, TALK_TIME, TALK_TYPE]

# 기다린 시간의 합이 최소가 되도록 각 상담 유형별로 멘토 인원을 정한다.
# answer: min(sum(기다린 시간))

import heapq

# 자연수 분할 함수 p(n, k)
# Brute Force (n <= 20)
def divide_natural(n, k):
    all_partition_list = []
    
    def dfs(rest_num, acc_len, acc_list):
        if acc_len == k - 1:
            all_partition_list.append(acc_list + [rest_num])
            return
        
        # (가능한 최대 숫자) = (남은 숫자) - (남은 acc 개수)
        for curr_num in range(1, rest_num - (k - acc_len - 1) + 1):
            dfs(rest_num - curr_num, acc_len + 1, acc_list + [curr_num])
    
    dfs(n, 0, [])
   

    return all_partition_list

# waiting time을 구하는 함수
# min_waiting_time: for back_tracking
# mentor_list: 각 유형별로 몇 명인지. (len: k)
def get_waiting_time(min_waiting_time: int, mentor_of_talk_type: list, reqs):
    
    waiting_dict = dict()           # waiting_line[talk_type] = [paricipant]
    mentor_dict = dict()            # 각 유형 별로 멘토 수 길이의 pq를 만듬.
    
    total_waiting_time = 0
    
    for talk_type in range(1, len(mentor_of_talk_type) + 1):
        mentor_dict[talk_type] = [0] * mentor_of_talk_type[talk_type - 1]
    
    for req_time, talk_time, talk_type in reqs:
        # 1. 참가자 req -> talk_type 멘토 중 상담 중이 아닌 멘토와 상담을 시작
        # 2. 멘토 모두 상담 중 -> 기다린 시간 = (상담 시작 시간) - (REQ_TIME)
        # 3. 멘토는 안 쉰다. 먼저 상담 요청한 참가자가 우선됨

        if mentor_dict[talk_type][0] <= req_time:
            heapq.heappop(mentor_dict[talk_type])
            heapq.heappush(mentor_dict[talk_type], req_time + talk_time)
        else:
            start_time = heapq.heappop(mentor_dict[talk_type])
            total_waiting_time += start_time - req_time
            heapq.heappush(mentor_dict[talk_type], start_time + talk_time)
            if total_waiting_time > min_waiting_time:
                return min_waiting_time
    
    return total_waiting_time

    
def solution(k, n, reqs):
    answer = 1e9
          
    for mentor_of_talk_type in divide_natural(n, k):
        answer = get_waiting_time(answer, mentor_of_talk_type, reqs)
        
    return answer
