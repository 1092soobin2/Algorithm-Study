def solution(word):

    power_5 = [781, 156, 31, 6, 1]
    assonance_dict = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    
    # A AA AAA AAAA 
    # AAAAA(5) AAAAE AAAAI AAAAO AAAAU(9)
    # AAAEA AAAEE AAAEI AAAEO AAAEU(14)
    
    answer = 0
    for idx, assonance in enumerate(word):
        answer += 1 + power_5[idx] * assonance_dict[assonance]
    
    return answer
