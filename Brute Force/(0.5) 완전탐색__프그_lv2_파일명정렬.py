from collections import defaultdict
def solution(files):
    answer = []
    #
    
    def split_file_name(file_name : str) -> list:
        head, number, tail = "", "", ""
        
        num_i_start, num_i_end = 0, 0
        for i_char, char in enumerate(file_name):
            if num_i_end != 0 and not char.isdigit():
                break
            if char.isdigit():
                # number의 처음인 경우 한 번만 저장
                if num_i_start == 0:
                    num_i_start = i_char
                # number인 경우 계속 갱신
                num_i_end = i_char + 1
        
        s, e = num_i_start, num_i_end
        return [file_name[:s], int(file_name[s:e]), file_name[e:]]
            
    
    # 대소문자를 구분하지 않는다.
    
    # head 별로 딕셔너리를 만든다.
    head_dict = defaultdict(list)       # {head: [[number, FILE_NAME], [...]], ...}
    for i_file, file in enumerate(files):
        head, number, tail = split_file_name(file)
        head_dict[head.lower()].append([number, i_file, tail, file])
        
    heads = list(head_dict.keys())
    heads.sort()
    for head in heads:
        head_dict[head].sort(key= lambda x : (x[0], x[1], x[2]))
        answer += list(zip(*head_dict[head]))[-1]
    
        
    return answer
