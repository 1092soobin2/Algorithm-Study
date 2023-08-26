import math

def solution(r1, r2):
    answer = 0
    # 1M
    # k * (r2^2 - k^2)^(1/2)
    
    for x in range(1, r2):
        if r1 >= x:
            n_dots = math.floor((r2**2 - x**2)**0.5) - math.ceil((r1**2 - x**2)**0.5) + 1      
        else:
            n_dots = math.floor((r2**2 - x**2)**0.5) + 1
        answer += n_dots
    answer = answer * 4 + 4
    
    return answer
