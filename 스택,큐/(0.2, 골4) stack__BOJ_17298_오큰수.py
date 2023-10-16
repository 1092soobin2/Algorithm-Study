# (0.2, 골4) BOJ_17298_오큰수

# 19:10~

# NgC(i) : 오른쪽에 있으면서 A_i도받 큰수 중 가장 왼쪽에 있는 수
#   A_i 가장 가까운 A보다 큰 수


N = int(input())
ARR = list(map(int, input().split()))

answer = [-1]*N
stack = []

for idx in range(N - 1, -1, -1):
    while stack:
        if ARR[idx] < stack[-1]:
            answer[idx] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(ARR[idx])

print(*answer)
