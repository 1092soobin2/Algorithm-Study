'''
pb:
divider = 1e9 + 7

에서 `int`로 안 감싸니까 틀림..


'''
K, P, N = map(int, input().split())

# 0 -> K
# 1 -> K * P
# 2 -> K * (P ** 2)
# ...
# N -> K * (P ** N)

# K * (P ** N) % (1e9 + 7)

divider = int(1e9 + 7)
#
# answer = K
# for _ in range(N):
#     answer = (answer * P) % divider

answer = K * pow(P, N, divider) % divider
print(answer)
