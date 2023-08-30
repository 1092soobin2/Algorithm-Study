# 21:50

# 장르별로 가장 많이 재생된 노래를
# 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며,
# 노래를 수록하는 기준은 다음과 같습니다.
    # 1. 속한 노래가 많이 재생된 장르 먼저 
    # 2. 장르 내에서 많이 재생된 노래 먼저
    # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
# genres: 노래의 장르를 나타내는 문자열 배열 
# plays: 노래별 재생 횟수를 나타내는 정수 배열 
# answer: 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로

from collections import defaultdict
import heapq
from typing import List, Dict

def solution(genres, plays):
    answer = []
    
    genre_play_dict     : Dict[int]         = defaultdict(int)
    genre_music_dict    : Dict[List[int]]   = defaultdict(list)
    
    # todo: range 구현
    # 장르 별 재생 횟수 집계, 장르 별 재생 음악 저장
    len_genres = len(genres)
    for i in range(len_genres):
        genre, play = genres[i], plays[i]
        genre_play_dict[genre] += play
        heapq.heappush(genre_music_dict[genre], (-play, i))
    
    # 재생 횟수 많은 순으로 장르 정렬
    genre_order_list = list(genre_play_dict.items())
    genre_order_list.sort(key=lambda x : -x[1])
    
    # 장르 별로 최대 2개 노래 추출
    for genre, _ in genre_order_list:
        if genre_music_dict[genre]:
            answer.append(heapq.heappop(genre_music_dict[genre])[1])
            # 최대 2개
            if genre_music_dict[genre]:
                answer.append(heapq.heappop(genre_music_dict[genre])[1])
    
    return answer
