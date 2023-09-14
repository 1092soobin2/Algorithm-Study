# ad-hoc == 최선의 전략을 떠올리기.

PERSON = 1
# 2*m 만큼 사용 가능

N, M = map(int, input().split())
town = list(map(int, input().split()))

num_of_wifi = 0

l_idx, r_idx = 0, 0
while r_idx < N:

    if r_idx - l_idx >= 2 * M and town[l_idx] == PERSON:
        l_idx = r_idx = r_idx + 1
        num_of_wifi += 1
    elif town[l_idx] != PERSON:
        l_idx = r_idx = l_idx + 1
    else:
        r_idx += 1

if l_idx != r_idx and town[l_idx] == PERSON:
    num_of_wifi += 1

print(num_of_wifi)

