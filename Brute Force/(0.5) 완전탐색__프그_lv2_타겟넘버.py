def solution(numbers, target):
    answer = 0
    
    ans = [0]
    def dfs(now_i, acc_num):
        
        if now_i == len(numbers):
            if acc_num == target:
                ans[0] += 1
            return
        
        dfs(now_i + 1, acc_num + numbers[now_i])
        dfs(now_i + 1, acc_num - numbers[now_i])
     
    dfs(0, 0)
    answer = ans[0]
    return answer
