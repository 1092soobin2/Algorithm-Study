def solution(cards):
    answer = 0
    
    # 총 100장 1-100 카드
    # 2-100 자연수를 정해 그 수 이하 카드 준비
    # 카드 수만큼 작은 상자를 준비
    
    # 상자 선택 하여 숫자 확인 (1)
    # 그 숫자에 해당하는 상자를 열어 숫자 확인(2)
    # 열어야 하는 상자 이미 열려 있을 때까지 반복 -> 1번 상자 그룹
    
    # 2번 상자 그룹 X -> 0
    # 2번 상자 그룹 O -> #(1 그룹) * #(2 그룹)
    
    num_cards = len(cards)
    cards = [0] + cards
    boxes_dict = dict(enumerate(cards))
    
    def one_round(first_box, opened):
        ret_cnt = 0
        
        # 처음 선택한 상자는 바로 열 수 있다.
        opened[first_box] = True
        ret_cnt += 1
        # 다음 상자를 확인한다.
        next_box = boxes_dict[first_box]
        
        while not opened[next_box]:
            opened[next_box] = True
            ret_cnt += 1
            next_box = boxes_dict[next_box]
        
        return ret_cnt
    
    opened_list = [False]*(num_cards+1)
    groups = []
    for i in range(1, num_cards+1):
        if not opened_list[i]:
            groups.append(one_round(i, opened_list))
        
    groups.append(0)
    groups.sort(key=lambda x : -x)
    
    # print(groups)
    answer = groups[0] * groups[1]
    return answer
