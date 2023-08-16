# (1) 구현__BOJ_16235_나무재테크
# 1. for문에서 dict 사용 중에 객체 수정 ㄴㄴ, 2. 시간 초과->

'''
NxN

양분
- 초기값 5

M trees

한 칸에 여러 개의 나무가 있을 수 있다.
1. 봄
- 자신의 나이만큼 양분을 먹으면 나이가 1 증가한다.
- 같은 칸의 양분만 먹을 수 있다.
- 나이가 어린 나무부터 양분을 먹는다.
- 자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽는다.
2. 여름
- 봄에 죽은 나무가 int(나이 / 2) 만큼의 양분으로 변한다.
3. 가을
- 나이가 5의 배수인 나무가 번식한다.
- 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
4. 겨울
- 모든 칸에 양분이 추가된다. A[r][c]

ans: K년 후의 나무의 개수를 구하는 프로그램

'''

# ===input===
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees_list = [list(map(int, input().split())) for _ in range(M)]     # r, c, age


def print_tree(arr):
    print("==============")
    for y in range(N):
        for x in range(N):
            print(arr[y][x], end=' ')
        print()
    print("==============")

# ===algorithm===
def add_tree(tree_row, tree_col, tree_age):
    global trees_dict
    if (tree_row, tree_col) in trees_dict:
        # 오름차순으로 순서 유지
        if tree_age == 1:
            trees_dict[(tree_row, tree_col)] = [1] + trees_dict[(tree_row, tree_col)][:]
        else:
            trees_dict[(tree_row, tree_col)].append(tree_age)
            trees_dict[(tree_row, tree_col)].sort()
    else:
        trees_dict[(tree_row, tree_col)] = [tree_age]



ground = [[5]*N for _ in range(N)]
trees_dict = dict()
for r, c, age in trees_list:
    add_tree(r-1, c-1, age)

# K년 반복
for order in range(K):

    dead_trees = dict()
    five_tree_locations = list()
    # 1. 봄
    for tree_location, tree_ages in trees_dict.items():
        r, c = tree_location
        for i, age in enumerate(tree_ages):
            if ground[r][c] >= age:
                ground[r][c] -= age
                # age += 1
                tree_ages[i] += 1
                if tree_ages[i] % 5 == 0:
                    five_tree_locations.append(tree_location)
            else:
                dead_trees[tree_location] = tree_ages[i:]
                trees_dict[tree_location] = tree_ages[:i]
                break
        trees_dict[tree_location].sort()

    # 2. 여름
    for tree_location, tree_ages in dead_trees.items():
        r, c = tree_location
        for age in tree_ages:
            ground[r][c] += age // 2

    # 3. 가을
    tmp_dict = dict(trees_dict)
    for tree_location in five_tree_locations:
        r, c = tree_location
        for dr, dc in [[-1, 0], [-1, -1], [0, -1], [1, -1],
                       [1, 0], [1, 1], [0, 1], [-1, 1]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                add_tree(nr, nc, 1)

    # 4. 겨울
    for r in range(N):
        for c in range(N):
            ground[r][c] += A[r][c]

    # print(order, "th")
    # print_tree(ground)

# ===output===
ans = 0
for tree_location, tree_ages in trees_dict.items():
    ans += len(tree_ages)
print(ans)