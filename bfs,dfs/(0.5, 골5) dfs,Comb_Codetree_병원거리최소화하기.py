# (1, 골5) Codetree_병원거리최소화하기

# 병원 거리 : min(병원거리)
# m개만 남겨야할 때, 각 사람들의 병원 거리의 총 합이 최소가 되도록

# comb(13, m) *1300
# 13*12*11 (10^3)
# 13*100 (10^3)

# === input ===
N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]
EMPTY, PERSON, HOSPITAL = 0, 1, 2
hospital_list = []
dist_list = []          # [person][hospital] -> [[[p0 h0, p0 h1,...], [p1 h0, 3, 4], ...]


# === algorithm ===
def init_ds():
    global hospital_list, dist_list

    for r in range(N):
        for c in range(N):
            if BOARD[r][c] == HOSPITAL:
                hospital_list.append([r, c])

    for r in range(N):
        for c in range(N):
            if BOARD[r][c] == PERSON:
                dist_list.append([])
                for hr, hc in hospital_list:
                    dist_list[-1].append(abs(r - hr) + abs(c - hc))

    if debug:
        print("hospital: ", hospital_list)
        print("dist: ", dist_list)


def comb(arr, r):
    comb_list = []

    def dfs(start_i, acc):
        if len(acc) == r:
            comb_list.append(acc)
            return
        for i in range(start_i, len(arr)):
            dfs(i + 1, acc + [arr[i]])

    dfs(0, [])
    return comb_list


def get_min_sum():
    ret_min_sum = 1e9

    for index_list in comb((range(len(hospital_list))), M):
        now_sum = 0
        for dist in dist_list:
            filtered = [dist[i] for i in index_list]
            now_sum += min(filtered)
        ret_min_sum = min(ret_min_sum, now_sum)

        if debug:
            print(index_list, now_sum)

    return ret_min_sum


# === output ===
debug = False

init_ds()
print(get_min_sum())
