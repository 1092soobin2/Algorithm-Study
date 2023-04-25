def solution(user_id, banned_id):
    answer = 0
    
    def get_possible_id_list(bid) -> list:
        ret_list = []
        
        for uid in user_id:
            if len(uid) != len(bid):
                continue
                
            flag = True
            for i in range(len(bid)):
                if bid[i] != "*":
                    flag &= (uid[i] == bid[i])
            if flag:
                ret_list.append(uid)
                
        return ret_list
    
    banned_list = []
    for bid in banned_id:
        
        banned_list.append(get_possible_id_list(bid))
    
    cases = set()
    def dfs(acc_num, acc_lst, total):
        if acc_num == total:
            case = tuple(sorted(set(acc_lst)))
            if len(case) == total:
                cases.add(case)
            return
        
        for bid in banned_list[acc_num]:
            if bid in acc_lst:
                continue
            dfs(acc_num+1, acc_lst + [bid], total)
            
    dfs(0, [], len(banned_id))
    answer = len(cases)
    
    return answer
