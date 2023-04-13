import sys
sys.setrecursionlimit(10000000)

def solution(words):
    answer = 0
    
    words.sort()
    N = len(words)
    
    def compare_nth_case(word_list, nth) -> list:
        ret_list = []
        len_of_word_list = len(word_list)
        
        nth -= 1        
        prev_i = 0
        for i in range(1, len_of_word_list):
            if word_list[i][nth] != word_list[i-1][nth]:
                ret_list.append(word_list[prev_i:i])
                prev_i = i
        ret_list.append(word_list[prev_i:len_of_word_list])
        
        return ret_list
        
    # Compare 1st case
    # word_list1 = compare_nth_case(words, 1)
    
#     # Compare 2nd case
#     word_list2 = []
#     for lst in word_list1:
#         if len(lst) == 1:
#             answer += 1
#             continue
#         word_list2 += compare_nth_case(lst, 2)
    
    
    
#     word_list3 = []
#     for lst in word_list2:
#         if len(lst) == 1:
#             answer += 2
#             continue
#         new_lst = []
#         for word in lst:
#             if len(word) == 2:
#                 answer += 2
#             else:
#                 new_lst.append(word)
#         word_list3 += compare_nth_case(new_lst, 2)
    
    prev_word_list = compare_nth_case(words, 1)
    prev_compare_case = 1
    while prev_word_list:
        next_word_list = []
        for lst in prev_word_list:
            # 1. 비교할 단어가 없으면 종료
            if len(lst) == 1:
                # 비교한 단어 만큼 추가
                answer += prev_compare_case
                continue
            # 2. 비교할 단어 O
            new_lst = []
            for word in lst:
                # 단어의 길이가 다음 비교 문자의 위치보다 작으면 종료
                if len(word) == prev_compare_case:
                    answer += prev_compare_case
                else:
                    new_lst.append(word)
            next_word_list += compare_nth_case(new_lst, prev_compare_case+1)
        
        # 갱신
        prev_word_list = next_word_list
        prev_compare_case += 1

        
    
    return answer
