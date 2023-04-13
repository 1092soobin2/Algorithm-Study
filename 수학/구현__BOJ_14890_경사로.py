# 구현__BOJ_14890_경사로
'''
NxN 지도
길: 일렬로 N칸

지나갈 수 있으려면 모든 칸의 높이가 같아야
경사로: 높이가 항상 1, 길이 L
- 낮은 칸에 놓아야 한다
- 높이 차가 1이어야 한다
-
'''

# ===input===
N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]


# ===algorithm===
def check_load(load: list) -> bool:
    # print(load)
    is_slope = [False] * N

    i = 1
    while i < N:
        if load[i] == load[i - 1]:
            i += 1
        elif load[i] - load[i - 1] == 1:
            j = 1
            while j <= L:
                if i-j >= 0 and not is_slope[i-j] and load[i-j] == load[i-1]:
                    j += 1
                else:
                    break
            if j > L:
                for k in range(1, L + 1):
                    is_slope[i-k] = True
                i += 1
            else:
                break
        elif load[i] - load[i - 1] == -1:
            j = 1
            # print("내려감")
            while j < L:
                if i+j < N and load[i] == load[i+j]:
                    j += 1
                else:
                    break
            if j >= L:
                for k in range(L):
                    is_slope[i + k] = True
                i += L
            else:
                break
        else:
            break

    # print(i)
    if i < N:
        return False
    else:
        return True


# ===output===
ans = 0
for r in range(N):
    # print()
    # 1. row
    if check_load(MAP[r]):
        ans += 1
    # 2. col
    tmp_load = []
    for c in range(N):
        tmp_load.append(MAP[c][r])
    if check_load(tmp_load):
        ans += 1
print(ans)
