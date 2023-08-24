def solution(number: str, k: int):
    
    # number에서 k개의 수를 제거했을 때
    # ans: 얻을 수 있는 가장 큰 숫자
    
    # Make number as List[int] type.   
    number_list = list(map(int, number))
    ans_number_list = []
    
    len_number = len(number)
    
    start_idx, end_idx = 0, k
    
    while (k > 0) and (end_idx < len_number):
        max_idx = start_idx
        for idx in range(start_idx, end_idx + 1):
            if number_list[idx] > number_list[max_idx]:
                max_idx = idx
            if number_list[idx] == 9:
                break
        
        # Add the maximum number to `ans_number_list`.
        ans_number_list.append(number_list[max_idx])
        
        # If the maximum number is forefront, add 1 to `start_idx`
        if (max_idx - start_idx) == 0:
            start_idx, end_idx = start_idx + 1, start_idx + 1 + k  
        # Remove the numbers in front of `max_idx`.
        else:   
            k -= (max_idx - start_idx)
            start_idx, end_idx = max_idx + 1, max_idx + 1 + k
    
    if k == 0:
        for rest_idx in range(max_idx + 1, len_number):
            ans_number_list.append(number_list[rest_idx])
            
    
    answer = "".join(map(str,ans_number_list))
    return answer
