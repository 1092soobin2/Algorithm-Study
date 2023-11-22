
# 23:04~
# term_type, available_duration

# 모든 달은 28일까지 있다고 가정한다.
# 오늘 날짜로 파기해야할 개인 정보 번호

# 숫자 리스트로 만들기
make_date = lambda x: list(map(int, x.split(".")))

# for date access
YEAR, MONTH, DAY = 0, 1, 2


def add_duration(date: list, duration: int) -> int:
    
    date[YEAR] += duration // 12
    date[MONTH] += duration % 12
    
    if date[MONTH] > 12:
        date[YEAR], date[MONTH] = date[YEAR] + 1, date[MONTH] - 12
    
    
# 유효 기간이면 True
def check_available(today, date) -> bool:
    
    if today[YEAR] > date[YEAR]:
        return False
    elif today[YEAR] < date[YEAR]:
        return True
    else:
        if today[MONTH] > date[MONTH]:
            return False
        elif today[MONTH] < date[MONTH]:
            return True
        else:
            if today[DAY] >= date[DAY]:
                return False
            else:
                return True
            
    
    
def solution(today, terms, privacies):
    answer = []
    
    # 딕셔너리화
    term_dict = dict()
    for term in terms:
        term_type, term_duration = term.split()
        term_dict[term_type] = int(term_duration)
    
    today = make_date(today)
    for num, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        date = make_date(date)
        # 기준 날짜 구하기
        add_duration(date, term_dict[term_type])
        # 비교하기
        if not check_available(today, date):
            answer.append(num + 1)
                    
    return answer
