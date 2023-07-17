import heapq

def solution(operations):
    answer = []
    deleted_set = set()
    min_q = []
    max_q = []

    for op in operations:
        if op[0] == "I":
            number = int(op[2:])
            if number in deleted_set:
                deleted_set.remove(number)
            heapq.heappush(min_q, number)
            heapq.heappush(max_q, -number)
        elif op[2] == "1":
            # 이미 삭제되었으면 힙큐에서 삭제
            while max_q and (-(max_q[0]) in deleted_set):
                heapq.heappop(max_q)
            if max_q:
                deleted_set.add(-(heapq.heappop(max_q)))
        elif op[2] == "-":
            while min_q and (min_q[0] in deleted_set):
                heapq.heappop(min_q)
            if min_q:
                deleted_set.add(heapq.heappop(min_q))
    
    while max_q and (-max_q[0] in deleted_set):
        heapq.heappop(max_q)
    while min_q and (min_q[0] in deleted_set):
        heapq.heappop(min_q)
        
    if min_q:
        answer.append(-max_q[0])
        answer.append(min_q[0])
    else:
        answer = [0, 0]
            
    return answer
