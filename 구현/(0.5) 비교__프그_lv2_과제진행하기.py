from collections import deque

def solution(plans):
    answer = []
    
    def process_plan(plan):
        h, m = map(int, plan[1].split(":"))
        t = int(plan[2])
        return [plan[0], h*60+m, t]
    
    plans = list(map(process_plan, plans))
    plans.sort(key=lambda x: (x[1]))
    
    waiting_queue = deque()
    last = 0
    num_plans = len(plans)
    for i in range(num_plans - 1):
        cur, nex = plans[i], plans[i+1]
        left_time = nex[1]-cur[1]
        # 과제 시작할 시각이 되면, 멈추고 시작
        if left_time < cur[2]:
            cur[2] -= left_time
            waiting_queue.append(cur)
        else:
            answer.append(cur[0])
            left_time -= cur[2]
            while left_time > 0 and waiting_queue:
                cur = waiting_queue.pop()
                if left_time < cur[2]:
                    cur[2] -= left_time
                    waiting_queue.append(cur)
                    break
                else:
                    answer.append(cur[0])
                    left_time -= cur[2]
                    
    answer.append(plans[num_plans-1][0])
    if waiting_queue:
        left = list(list(zip(*waiting_queue))[0])
        answer += left[::-1]
                    
        
    return answer
