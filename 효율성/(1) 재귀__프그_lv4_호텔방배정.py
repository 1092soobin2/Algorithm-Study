import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    answer = []
    
    room_dict = dict()
    
    def find_empty(room_num):
        # 빈 방 이면
        if room_num not in room_dict:
            # 배정
            if room_num+1 in room_dict:
                room_dict[room_num] = room_dict[room_num+1]
            else:
                room_dict[room_num] = room_num+1
            return room_num
            
        # 사용 중이면 다음 번호 배정  
        empty_room = find_empty(room_dict[room_num])
        room_dict[room_num] = room_dict[empty_room]
        return empty_room
        
            
    for num in room_number:
        answer.append(find_empty(num))
                
    
    return answer
