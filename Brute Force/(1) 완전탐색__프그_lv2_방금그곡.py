def solution(m, musicinfos):
    answer = ''
    
    # start_time, end_time, name, sheets
    # 12 notes
    # 음악은 항상 처음부터 재생된다.
    # 음악이 00:00을 넘겨서 재생되는 일은 없다.
    
    def make_int_time(str_time):
        h, m = map(int, str_time.split(":"))
        return h*60 + m
    
    def pre_process_melody(melody):
        melody = melody.replace("C#", "H")
        melody = melody.replace("D#", "I")
        melody = melody.replace("F#", "J")
        melody = melody.replace("G#", "K")
        melody = melody.replace("A#", "L")
        return melody
        
    answer = ""
    answer_time = 0
    m = pre_process_melody(m)
    
    for musicinfo in musicinfos:
        start_time, end_time, name, sheets = musicinfo.split(",")
        # 재생된 멜로디 만들기
        play_time = make_int_time(end_time) - make_int_time(start_time)
        sheets = pre_process_melody(sheets)
        len_music = len(sheets)
        play_music = ""
        while play_time > 0:
            play_music += sheets[:play_time]
            play_time -= len_music
        
        # 재생된 멜로디에 m이 있는 확인
        if play_music.find(m) != -1:
            # 여러 개면 (제일 긴 음악)
            if len(play_music) > answer_time:
                answer_time = len(play_music)
                answer = name
    
    # 없으면 (None)  
    if not answer:
        answer = "(None)"
        
    return answer
