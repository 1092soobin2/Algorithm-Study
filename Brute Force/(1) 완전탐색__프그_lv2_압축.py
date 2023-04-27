def solution(msg):
    answer = []
    
    LEN_MSG = len(msg)
    LZW_id = 1
    LZW_dict = dict()
    
    def get_id(char: str) -> int:
        if char in LZW_dict:
            return LZW_dict[char]
        else:
            LZW_dict[char] = LZW_id
            return LZW_id + 1
    
    def find_longest(index: int) -> int:
        string = msg[index]
        new_id = get_id(string)
        # 가장 긴 문자열 찾기
        prev_id = new_id
        index += 1
        # w가 사전에 있으면 (string_id < LZW_id) 다음 글자도 포함시켜서 탐색
        while new_id < LZW_id and index < LEN_MSG:
            prev_id = new_id
            string += msg[index]
            new_id = get_id(string)
            index += 1
        
        next_index = index - 1
        if new_id < LZW_id:
            prev_id = new_id
            new_id = LZW_id
            next_index = index
        # print(string, next_index)
        return prev_id, new_id, next_index
    # 1. 길이가 1인 모든 단어
    for i in range(26):
        LZW_id = get_id(chr(ord('A') + i))
    
    # 2. 현재 입력과 일치하는 가장 긴 문자열 w
    i_msg = 0
    while i_msg < LEN_MSG:
        w_id, LZW_id, i_msg = find_longest(i_msg)
        answer.append(w_id)
    return answer
