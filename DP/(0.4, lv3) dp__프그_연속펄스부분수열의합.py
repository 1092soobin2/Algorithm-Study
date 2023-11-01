# 22:00 ~
# 연속 펄스 부분 수열 = (연속 부분 수열) * (펄스 수열) (element-wise)

def solution(sequence):
    
    LEN_SEQ = len(sequence)
    seq1 = [sequence[i] * (-1) ** i for i in range(LEN_SEQ)]
    seq2 = [num * (-1) for num in seq1]
    
    def get_max(seq):
        
        dp = [0]*LEN_SEQ
        dp[0] = max(dp[0], seq[0])
        
        for i in range(1, LEN_SEQ):
            dp[i] = max(dp[i-1], 0) + seq[i]
            
        return max(dp)
    
    return max(get_max(seq1), get_max(seq2))
