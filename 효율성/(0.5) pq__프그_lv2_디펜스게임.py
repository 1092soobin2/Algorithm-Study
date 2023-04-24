import heapq

def solution(n, k, enemy):
    answer = 0
    
    # 무적권 개수 >= 라운드
    rounds = len(enemy)
    if k >= rounds:
        return rounds
    
    pq_maxes = []
    num_enemy = 0
    for i in range(k):
        heapq.heappush(pq_maxes, enemy[i])

    answer = k
    for i in range(k, rounds):
        # 만약 제일 작은 maximum보다 크다면 교체
        if pq_maxes[0] < enemy[i]:
            num_enemy += heapq.heappop(pq_maxes)
            heapq.heappush(pq_maxes, enemy[i])
        else:
            num_enemy += enemy[i]
        # print(i+1, num_enemy)
        if num_enemy <= n:
            answer = i+1
        else:
            break
        
    return answer
