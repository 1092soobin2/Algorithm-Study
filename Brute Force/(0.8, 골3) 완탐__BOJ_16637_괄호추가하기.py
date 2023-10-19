# (0.5, 골3) BOJ_16637_괄호추가하기

# N 길이의 수식
# 0 <= 정수 <= 9
# 연산자 (+, -, x)

N = int(input())
expression = input()


def init():
    global expression
    expression = list(expression)

    for i in range(0, N, 2):
        expression[i] = int(expression[i])


def calculate(expr):

    digit = expr[0]
    for operator_idx in range(1, len(expr), 2):
        operator = expr[operator_idx]
        next_digit = expr[operator_idx + 1]
        if operator == '+':
            digit += next_digit
        elif operator == '-':
            digit -= next_digit
        elif operator == '*':
            digit *= next_digit

    return digit


def dfs(start_idx, expr, len_expr):
    global answer

    answer = max(answer, calculate(expr))

    if start_idx > len_expr - 2:
        return
    for idx in range(start_idx, len_expr, 2):
        # 괄호 O
        new_expr = expr[:idx - 1] + [calculate(expr[idx - 1:idx+2])] + expr[idx + 2:]
        dfs(idx + 2, new_expr, len_expr - 2)


answer = -int(1e9)


def solution():
    init()
    if N == 1:
        return expression[0]

    dfs(1, expression, N)

    return answer


print(solution())
