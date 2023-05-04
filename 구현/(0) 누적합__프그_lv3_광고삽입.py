from collections import defaultdict
def solution(str1, str2):
    answer = 0
    
    # 1. 딕셔너리로 만들기
    dict1, dict2 = defaultdict(int), defaultdict(int)
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            dict1[str1[i:i+2].lower()] += 1
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            dict2[str2[i:i+2].lower()] += 1
    

    # 2. 교집합: 중복되는 키 찾아서 min개수 합치키
    # 3. 합집합
    intersection = dict()
    union = dict()
    for s in dict1:
        if s in dict2:
            intersection[s] = min(dict1[s], dict2[s])
            union[s] = max(dict1[s], dict2[s])
        else:
            union[s] = dict1[s]
    for s in dict2:
        if s in dict1:
            intersection[s] = min(dict1[s], dict2[s])
            union[s] = max(dict1[s], dict2[s])
        else:
            union[s] = dict2[s]
    
    frac_up, frac_down = sum(intersection.values()), sum(union.values())
    if frac_down == 0:
        answer = 65536
    else:
        answer = int((frac_up/frac_down)*65536)
    return answer
