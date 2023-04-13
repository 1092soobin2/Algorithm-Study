def solution(n, t, max_people, timetable):
    answer = ''
    # 09:00, 09:00 + t, 09:00 + 2*t, ... 09:00 + (n-1)*t
    
    lines = [0]*n
    last_line = []
    
    def get_int_time(str_time: str):
        h, m = map(int, str_time.split(":"))
        return h*60 + m
    
    # 줄 세우기
    timetable.sort()
    i_line = 0
    i_time = 0
    num_of_crew = len(timetable)
    while i_line < n and i_time < num_of_crew:
        shuttle_time = 9*60 + i_line*t
        crew_time = get_int_time(timetable[i_time])
        # 크루를 태우는 경우, 크루도착 시간 <= 셔틀 시간
        if crew_time <= shuttle_time:
            lines[i_line] += 1
            i_time += 1
            # 마지막 라인이면 크루의 시간도 저장
            if i_line == n-1:
                last_line.append(crew_time)
            # 크루를 태웠는데 버스가 꽉 차면 출발
            if lines[i_line] == max_people:
                i_line += 1
        else:
            i_line += 1

    # 마지막 칸이 비었으면 (그 시간)
    if lines[-1] < max_people:
        answer_time = 9*60 + (n-1)*t
    # 비어 있는 칸이 없으면 (마지막 시간 사람들 중 제일 늦은 시각 - 1분)
    else:
        answer_time = last_line[-1] - 1
    
    h, m = answer_time // 60, answer_time % 60
    answer = f"{h:02}:{m:02}"
        
            
    return answer
