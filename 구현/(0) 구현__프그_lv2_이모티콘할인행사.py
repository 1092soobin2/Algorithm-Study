# 23:32~

# 1. 서비스 가입자 늘리기
# 2. 이모티콘 판매액 늘리기

# n명에게 m개 할인
# 이모티콘 - 할인율

# answer: 목적을 최대한 달성한 가입자수, 매출액

# users: [proportion, price]

import heapq


def decide_all_users(users, emoticons, emoticon_promotion):
    
    def decide_one_user(user):
        
        # 다음 기준에 따라 이모티콘을 사거나(2) 서비스에 가입(1)
        proportion, price = user

        total_buy = 0
        # - 자신의 기준에 따라, 일정 비율 이상 할인하는, 이모티콘 모두 구매
        for emoticon, promotion in zip(emoticons, emoticon_promotion):
            if promotion >= proportion:
                total_buy += emoticon * (100 -promotion) / 100
        
        # - 이코티콘 구매 비용의 합이 일정 가격 이상이라면, 모두 취소하고 서비스 가입
        if total_buy >= price:
            return [1, 0]
        else:
            return [0, total_buy]
    
    all_result = [0, 0]
    for user in users:
        one_result = decide_one_user(user)
        all_result[0] += one_result[0]
        all_result[1] += one_result[1]
    # print(emoticon_promotion, all_result)
    return all_result


def solution(users, emoticons):

    answer_pq = []
    
    def brute_force(acc):
        
        if len(acc) == len(emoticons):
            result = decide_all_users(users, emoticons, acc)
            heapq.heappush(answer_pq, (-result[0], -result[1]))
            return
        
        for acc_int in [10, 20, 30, 40]:
            brute_force(acc + [acc_int])
    
    brute_force([])
    answer = answer_pq[0]
    answer = [-answer[0], -answer[1]]
    
    return answer
    # return answer_pq
