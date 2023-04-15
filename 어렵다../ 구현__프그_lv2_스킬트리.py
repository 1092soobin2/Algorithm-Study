from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0
    
    num_skill = len(skill)
    
    skill_dict = dict()
    for i in range(num_skill):
        skill_dict[skill[i]] = set(list(skill[i+1:i+2]))
    
    for tree in skill_trees:
        tree = list(filter(lambda x: x in skill_dict, list(tree)))
        
        # 선행 스킬이 필요없느 스킬들로만 이루어져 있는 트리
        if not tree:
            answer += 1
        # 트리스킬[0]이 skill[0]이 아닌 경우 
        elif tree[0] != skill[0]:
            continue
        else:
            is_possible = True
            prev_skill = tree[0]
            for i_tree in range(1, len(tree)):
                if prev_skill == tree[i_tree]:
                    pass
                elif tree[i_tree] in skill_dict[prev_skill]:
                    prev_skill = tree[i_tree]
                else:
                    is_possible = False
                    break
            if is_possible:
                answer += 1
                    
        
    return answer
