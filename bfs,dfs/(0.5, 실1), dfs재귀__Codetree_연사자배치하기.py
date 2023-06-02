# (0.5, 실1), __Codetree_연사자배치하기

# +, -, x

# 3*3*3... 3^10 ->(3^2)^5 ~ 10^5


# === input ===
n = int(input())
ADD, SUB, MULT = 0, 1, 2
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))


# === algorithm ===
def solution():
    result_list = []

    def dfs(itr, op_list, acc):

        # 계산 완료
        if itr == n:
            result_list.append(acc)
            return

        # 연산자 하나씩 시도하기
        if op_list[ADD] > 0:
            op_list[ADD] -= 1
            dfs(itr + 1, op_list, acc + num_list[itr])
            op_list[ADD] += 1

        if op_list[SUB] > 0:
            op_list[SUB] -= 1
            dfs(itr + 1, op_list, acc - num_list[itr])
            op_list[SUB] += 1

        if op_list[MULT] > 0:
            op_list[MULT] -= 1
            dfs(itr + 1, op_list, acc * num_list[itr])
            op_list[MULT] += 1

    dfs(1, operator_list, num_list[0])

    return min(result_list), max(result_list)


# === output ===
print(*solution())
