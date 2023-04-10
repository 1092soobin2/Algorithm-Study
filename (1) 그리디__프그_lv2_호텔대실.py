def solution(book_time: list):    
    answer = 0
    # ans: 필요한 최소 객실 수
    
    # [start_time, end_time]
    # end_time + 10부터 사용할 수 있음.

    
    def make_int_time(str_time: str):
        hour, minute = map(int, str_time.split(":"))
        return hour*60 + minute

    book_time = [list(list(map(make_int_time, times))) for times in book_time]
    book_time.sort(key=lambda x : x[0])
    
    end_times = [0]
    num_of_rooms = len(end_times)
    for start_time, end_time in book_time:
        change_flag = False
        for i in range(num_of_rooms):
            if end_times[i] < start_time:
                change_flag = True
                end_times[i] = end_time+9
                break
        if not change_flag:
            end_times.append(end_time+9)
            num_of_rooms += 1
            
    answer = num_of_rooms
    return answer
