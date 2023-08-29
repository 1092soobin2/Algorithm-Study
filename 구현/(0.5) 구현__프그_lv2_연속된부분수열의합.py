def solution(sequence, k):
    answer = []
    
    # sequence: 수열
    # sum(부분 sequence) == k
    # k가 여려 개인 경우 길이가 짧은 수열
    # 길이가 짧은 수열이 여러 개인 경우 앞쪽
    
    len_sequence = len(sequence)
    
    right_idx = -1
    curr_sum = 0
    for idx in range(len_sequence-1, -1, -1):
        if sequence[idx] > k :
            continue
        elif sequence[idx] == k:
            answer = [idx, idx]
        else:
            # sequence에 k가 있으면 종료
            if answer and answer[0] == answer[1]:
                break
                
            # 처음 체크하는 경우
            if curr_sum == 0:
                curr_sum = sequence[idx]
                right_idx = idx
            else:
                if curr_sum + sequence[idx] > k:
                    curr_sum -= sequence[right_idx]
                    right_idx -= 1
                    curr_sum += sequence[idx]
                elif curr_sum + sequence[idx] == k:
                    if answer and (answer[1] - answer[0]) < (right_idx - idx):
                        break
                    answer = [idx, right_idx]
                    
                    curr_sum -= sequence[right_idx]
                    right_idx -= 1
                    curr_sum += sequence[idx]
                else:
                    if answer and (answer[1] - answer[0]) < (right_idx - idx):
                        break
                    curr_sum += sequence[idx] 
            
    return answer
