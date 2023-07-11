def solution(routes):
    answer = 0
    
    # routes : 차량의 경로
    # 진입, 진출 지점 -30000 ~ +30000
    
    routes.sort(key=lambda x : (x[0], x[1]))
    print(routes)
    
    prev_camera = routes[0][1]
    answer += 1
    
    for start, end in routes:
        # 겹치는 부분이 있는 경우
        if start <= prev_camera:
            prev_camera = min(prev_camera, end)
        else:
            prev_camera = end
            answer += 1
        print(prev_camera)
    return answer
