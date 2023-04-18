import heapq

def solution(n, works):
    answer = 0
    
    # (야근 피로도) = (야근 시작 시점부터 남은 일)들의 제곱 합
    # n 시간 동안 야근 피로도를 최소화하도록
    
    num_works = len(works)
    works = list(map(lambda x : -x, works))
    heapq.heapify(works)
    
    while n > 0 :
        max_work = heapq.heappop(works)
        if max_work == 0:
            break
        n -= 1
        heapq.heappush(works, max_work + 1)
        
        
    
    answer = sum(map(lambda x : x**2, works))
        
    return answer
