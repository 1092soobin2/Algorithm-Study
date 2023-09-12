# (0.5, 골3) Codetree_보도블럭

# 경사로 1 * L
# N*N grid

# 경사로를 못 놓는 경우
# - 높이가 1 이상 차이 나는 경우
# - L 미만의 보도 블럭이 연속하는 경우
# - 경사로를 놓은 곳에 또 경사로를 놓은 경우


N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def check_line(line) -> bool:

    num_of_same_block = 1
    i = 1
    while i < N:
        if line[i - 1] == line[i]:
            num_of_same_block += 1
            i += 1
        elif line[i - 1] - line[i] == 1:    # 낮아지는 경우
            if i + L <= N:                  # 남은 블럭이 L 이상인지 확인
                for j in range(i + 1, i + L):
                    if line[j] != line[i]:  # 다음에 등장하는 블럭들이 같은 높이인지 확인
                        return False
                i += L
                num_of_same_block = 0
            else:
                return False
        elif line[i - 1] - line[i] == -1:   # 높아지는 경우
            if num_of_same_block >= L:
                num_of_same_block = 1
                i += 1
            else:
                return False
        else:                               # 1칸 초과 높이 차이
            return False
    return True


def solution():

    answer = 0
    for r in range(N):
        if check_line(grid[r]):
            answer += 1
    for c in range(N):
        if check_line([grid[r][c] for r in range(N)]):
            answer += 1
    return answer


print(solution())
