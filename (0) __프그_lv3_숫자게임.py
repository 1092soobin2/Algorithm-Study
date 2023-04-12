def solution(A, B):
    answer = 0
    
    # 숫자가 큰 쪽이 승리 -> 승점 1점
    # 숫자가 같다면 무승부
    A.sort()
    B.sort()
    a_i, b_i = 0, 0
    num = len(A)
    
    while a_i < num and b_i < num:
        if B[b_i] > A[a_i]:
            a_i += 1
            answer += 1
        b_i += 1
        
            
    return answer
