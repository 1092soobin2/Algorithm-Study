# (0.3, lv3) Softeer_순서대로방문하기

N = int(input())
lecture_list = [list(map(int, input().split())) for _ in range(N)]

# 1. fin 기준으로 정렬
lecture_list.sort(key=lambda x: x[1])
# 2. greedy
max_num_lecture = 0
prev_finish = 0
for start, finish in lecture_list:
    if prev_finish <= start:
        prev_finish = finish
        max_num_lecture += 1

print(max_num_lecture)
