def solution(targets):
    answer = 0  # 모두 요격하는, 최소 미사일 개수
    # (s, e) -> s < x < e 에서 발사하는 미사일로 요격 O
    
    targets.sort(key=lambda x : (x[0], x[1]))
    # 이전 미사일의 끝나는 지점 저장
    prev_e = 0
    for s, e in targets:
        # 이전 미사일의  끝지점 보다 앞서면 갱신, 요격 미사일 1개 추가
        if prev_e <= s:
            answer += 1
            prev_e = e
        # 이전 미사일의 끝지점 보다 앞선 끝지점이면 갱신
        if e < prev_e:
            prev_e = e

        
        
    return answer
