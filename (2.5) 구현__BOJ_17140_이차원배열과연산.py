# (2.25) 구현__BOJ_17140_이차원배열과연산 2
# list().sort -> None.sort() >>>>>>>list()로 생성된 객체는 변수에 할당하지 않으면 참조할 수 없다.
'''

3x3 A
R -> n(row) >= n(col)인 경우에 행에 대해 정렬
C -> n(row) <  n(col)인 경우에 열에 대해 정렬

정렬 방법
    1. 수의 등장 횟수
    2. 수
    배열 -> (수, 등장 횟수) ...
    key = 등장 횟수(오름차순) -> 수(오름차순)

- 0은 무시한다.
- 행, 열의 크기가 100이 넘으면 나머지는 버린다.

ans: A[r][c] == k 가 되는 최소 시간 (100 초과이면 -1)
'''

# from functools import reduce
# ===input===
input_r, input_c, input_k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]


# ===algorithm===
def print_A():
    global A
    for r in range(num_of_row):
        for c in range(num_of_col):
            print(A[r][c], end=' ')
        print()


def add_to_dict(dictionary: dict, number:int):
    if number == 0:
        pass
    elif number in dictionary:
        dictionary[number] += 1
    else:
        dictionary[number] = 1


def check_boundary(index_row, index_col):
    return 0 <= index_row < num_of_row and 0 <= index_col < num_of_col


ans = 0
num_of_row, num_of_col = 3, 3
input_r, input_c = input_r-1, input_c-1
while ans <= 100:
    # 100 초과는 버린다.
    if num_of_row > 100:
        A = A[:100]
        num_of_row = 100
    if num_of_col > 100:
        for r in range(num_of_row):
            A[r] = A[r][:100]
        num_of_col = 100

    if 0 <= input_r < num_of_row and 0 <= input_c < num_of_col and A[input_r][input_c] == input_k:
        break

    # num_count_dict = dict()
    # R 연산
    if num_of_row >= num_of_col:
        max_col = num_of_col
        # 1. 정렬
        for r in range(num_of_row):
            # 1) 수, 등장 횟수 세기
            num_count_dict = dict()
            for c in range(num_of_col):
                add_to_dict(num_count_dict, A[r][c])
            # 2) 리스트로 만들기
            new_row = sum(sorted(list(map(list, num_count_dict.items())), key=lambda x: (x[1], x[0])), [])
            A[r] = new_row
            # 3) column 개수 갱신
            max_col = max(max_col, len(new_row))
        # 2. 0 채우기
        num_of_col = max_col
        for r in range(num_of_row):
            A[r] += [0] * (num_of_col-len(A[r]))

    # C 연산
    else:
        max_row = num_of_row
        # 1. 정렬
        for c in range(num_of_col):
            num_count_dict = dict()
            for r in range(num_of_row):
                add_to_dict(num_count_dict, A[r][c])
            new_col = sum(sorted(list(map(list, num_count_dict.items())), key=lambda x: (x[1], x[0])), [])
            max_row = max(max_row, len(new_col))
            if max_row > len(A):
                len_of_A = len(A)
                A += [[0]*num_of_col for _ in range(max_row-len_of_A)]
            # for r in range(len(new_col)):
            for r in range(max_row):
                if r < len(new_col):
                    A[r][c] = new_col[r]
                else:
                    A[r][c] = 0
            # if ans == 4 and c == 1:
            #     print(num_count_dict)
            #     print(new_col)
            #     print_A()
            #     exit()
        # 2. 0 채우기. (위에서 채워짐)
        num_of_row = max_row
    ans += 1

# ===output===
# print(ans)
print(ans if ans <= 100 else -1)