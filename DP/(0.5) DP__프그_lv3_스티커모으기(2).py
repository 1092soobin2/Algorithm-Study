def solution(sticker):
    answer = 0
          
    num_of_stickers = len(sticker)
    if num_of_stickers <= 3:
        answer = max(sticker)
    elif num_of_stickers == 4:
        answer = max(sticker[0]+sticker[2] + sticker[1]+sticker[3])
    else:
        dp = [0]*num_of_stickers
        dp[0] = sticker[0]
        dp[1] = sticker[1]
        dp[2] = max(dp[0]+ sticker[2], dp[1])
        for i in range(3, num_of_stickers):
            dp[i] = max(dp[i-2] + sticker[i], dp[i-3]+ sticker[i], dp[i-1])

        dp2 = [0]*num_of_stickers
        dp2[0] = 0
        dp2[1] = sticker[1]
        dp2[2] = max(dp2[0]+ sticker[2], dp2[1])
        for i in range(3, num_of_stickers):
            dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-3]+ sticker[i], dp2[i-1])

        answer = max(dp[num_of_stickers-2], dp2[num_of_stickers-1])
        # print(sticker)
        # print(dp)
        # print(dp2)
    return answer
