# (0.2, 실2) BOJ_1182_부분수열의합


# N개 정수 수열
# 부분 수열 중 더한 값이 S가 되는
from itertools import combinations


N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 20 C 1 + ... = 2 ^ 20 = 10 ^ 6
answer = 0
for len_sub_sequence in range(1, N + 1):
    for sub_sequence in combinations(arr, len_sub_sequence):
        # print(sub_sequence)
        if sum(sub_sequence) == S:
            answer += 1

print(answer)
