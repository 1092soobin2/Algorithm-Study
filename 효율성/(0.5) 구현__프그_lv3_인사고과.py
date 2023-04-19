def solution(scores):
    answer = 1
    
    wanho_score = scores[0]
    wanho_sum = sum(wanho_score)
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    max_colleague = 0
    for score in scores:
        if wanho_score[0] < score[0] and wanho_score[1] < score[1]:
            return -1
        if score[1] >= max_colleague:
            max_colleague = score[1]
            if wanho_sum < sum(score):
                answer += 1
            
    return answer
