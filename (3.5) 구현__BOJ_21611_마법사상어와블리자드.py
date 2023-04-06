# (3.5) 구현__BOJ_21611_마법사상어와블리자드
# arr길이가 0, 1, 2인 경우 ㅜㅜㅜㅠ...제발....
# 1. IndexError 주의 / 2. 처음과 마지막 요소 처리에 주의

# 1, 2, 3 balls
# 연속하는 구슬: 같은 번호 구슬이 연속하여 있음
# blizard: d, s


# 4. M번 반복
# ans: 1*(num_of_exploded[0]) + 2*...[1] + 3*...[2]


# ===input===
N, M = map(int, input().split())
input_array = [list(map(int, input().split())) for _ in range(N)]
blizards = [list(map(int, input().split())) for _ in range(M)]


# ===algorithm===
# TODO: 폭발 구슬들
num_of_exploded = [0, 0, 0, 0]

# Constants
DIRECTION_LIST = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
SHARK_LOC = int(N/2)
location_id_dict = dict()


# 0. 1차원으로 만들기, location_dict 만들기
def make_array_1d_and_location_dict(array_2d) -> (list, list):
    # Return values
    array_1d = [0, ]                    # 0번 자리에는 상어가 있다.
    location_dictionary = dict()

    # Local variables
    direction_order = [3, 2, 4, 1]
    r = c = SHARK_LOC
    d_id = 0
    location_id = 1

    # 11 22 33 44 55 ... N-1N-1N-1
    for num_of_forward in range(1, N):
        num_of_repeat = 2
        if num_of_forward == N-1:
            num_of_repeat = 3
        for _ in range(num_of_repeat):
            for _ in range(num_of_forward):
                dr, dc = DIRECTION_LIST[direction_order[d_id]]
                r, c = r+dr, c+dc
                location_dictionary[(r, c)] = location_id
                if array_2d[r][c] != 0:
                    array_1d.append(array_2d[r][c])
                location_id += 1
            d_id = (d_id+1) % 4

    return array_1d, location_dictionary


# 1. 구슬 파괴
# TODO: 파괴-> del list[i]
def destroy_marbles(arr, direction_id, strength):
    r = c = SHARK_LOC
    dr, dc = DIRECTION_LIST[direction_id]
    destoryed_id_list = []
    for _ in range(strength):          # 조건 상 경계 넘어갈 일 없다.
        r, c = r+dr, c+dc
        loc_id = location_id_dict[(r, c)]
        if loc_id >= len(arr) or arr[loc_id] == 0:
            break
        destoryed_id_list.append(loc_id)
    # location_id가 큰 순서대로 구슬을 파괴한다.
    for loc_id in destoryed_id_list[::-1]:
        del arr[loc_id]
    return arr


# 2. 다 채워질 때까지 반복
    # 1. 구슬 이동 (저절로 된당.)
    # 2. 구슬 폭발: 4개 이상 연속하는 구슬들
def explode_marbles(arr):
    while True:
        exploded_list = []          # (loc_id(start), num_of_marbles)
        # 폭발 구슬들 찾기
        num_of_marbles = 1
        for loc_id in range(2, len(arr)):
            if arr[loc_id] == arr[loc_id-1]:
                num_of_marbles += 1
                if loc_id == len(arr)-1 and num_of_marbles >= 4:
                    exploded_list.append((loc_id-num_of_marbles+1, num_of_marbles))
            else:
                if num_of_marbles >= 4:
                    exploded_list.append((loc_id-num_of_marbles, num_of_marbles))
                num_of_marbles = 1
        # 폭발할 구슬들이 없으면 멈춤
        if not exploded_list:
            break
        # 뒤에서부터 폭발
        for loc_id, num in exploded_list[::-1]:
            num_of_exploded[arr[loc_id]] += num
            arr = arr[:loc_id] + arr[loc_id+num:]
    return arr


# 3. 구슬 변화
    # 1. A(구슬 개수), B(구슬 번호)
    # 2. 구슬 칸의 수보다 많으면 뒤에 구슬들은 버려짐.
def change_marbles(arr):
    num_id_pairs = []
    if len(arr) == 1:
        pass
    elif len(arr) == 2:
        num_id_pairs.append([1, arr[1]])
    else:
        num_of_marbles = 1
        for loc_id in range(2, len(arr)):
            if arr[loc_id] == arr[loc_id - 1]:
                num_of_marbles += 1
            else:
                num_id_pairs.append([num_of_marbles, arr[loc_id-1]])
                num_of_marbles = 1

        # 마지막 구슬 추가 안 되었을 수 있음.
        last_id = len(arr) - 1
        if arr[last_id] != arr[last_id - 1]:
            num_id_pairs.append([1, arr[last_id]])
        elif arr[last_id] == arr[last_id - 1]:
            num_id_pairs.append([num_of_marbles, arr[last_id]])

    new_arr = [0] + sum(num_id_pairs, [])
    arr = new_arr[:N*N]
    return arr


# ===output===
marbles, location_id_dict = make_array_1d_and_location_dict(input_array)
for d, s in blizards:
    marbles = destroy_marbles(marbles, d, s)
    # print(len(marbles), " ", marbles)
    marbles = explode_marbles(marbles)
    # print(len(marbles), " ", marbles)
    marbles = change_marbles(marbles)
    # print(len(marbles), " ", marbles, "\n")

# print(num_of_exploded)
ans = sum([i*val for i, val in enumerate(num_of_exploded)])
print(ans)