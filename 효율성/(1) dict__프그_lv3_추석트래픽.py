from collections import defaultdict

def solution(lines):
    answer = 0
    
    DAY = 24*60*60*1000
    MINUTE = 60
    SEC = 60
    MSEC = 1000
    
    # amount = [0] * (DAY + 1)
    amount_dict = defaultdict(int)
    
    # "S T"
    def calculate_time(time_str) -> int:
        hour, minute, sec = map(float, time_str.split(":"))
        hour *= MINUTE*SEC*MSEC
        minute *= SEC*MSEC
        sec *= MSEC
        return int(sum([hour, minute, sec]))
    
    def calculate_elapsed(time_str) -> int:
        sec = float(time_str[:-1])
        sec *= MSEC
        return int(sec)
     
    min_start = DAY
    max_end = 0
    
    for line in lines:
        _, time, elapsed = line.split()
        end_time = calculate_time(time)
        elapsed = calculate_elapsed(elapsed)
        
        start_time = (end_time + 1 - elapsed) - 999
        if start_time < 0:
            start_time = 0
        
        # print(start_time, end_time)
        for i in range(start_time, end_time+1):
            amount_dict[i] += 1
            answer = max(answer, amount_dict[i])
    return answer
