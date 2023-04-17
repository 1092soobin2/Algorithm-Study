def solution(places):
    answer = []
    
    EMPTY = 'O'
    PARTITION = 'X'
    PERSON = 'P'
    
    # 5x5 place
    
    def check_one_place(place) -> bool:
        
        people = []
        # 1. 사람들 위치 저장
        for r in range(5):
            for c in range(5):
                if place[r][c] == PERSON:
                    people.append([r, c])
        
        # 2. 사람1 - 모든 사람 페어 검사
        for p1 in people:
            for p2 in people:
                if p1 == p2:
                    continue
                [r1, c1], [r2, c2] = p1, p2
                # 두 사람 간의 거리가 2 이하이면 검사
                if abs(r1-r2) + abs(c1-c2) == 1:
                    return False
                elif abs(r1-r2) + abs(c1-c2) == 2:
                    if abs(r1-r2) == 2:
                        if place[(r1+r2)//2][c1] != PARTITION:
                            return False
                    elif abs(c1-c2) == 2:
                        if place[r1][(c1+c2)//2] != PARTITION:
                            return False
                    else:
                        if place[r1][c2] != PARTITION or place[r2][c1] != PARTITION:
                            return False
        return True
    
    for place in places:
        if check_one_place(place):
            answer.append(1)
        else:
            answer.append(0)
                        
                        
    return answer
