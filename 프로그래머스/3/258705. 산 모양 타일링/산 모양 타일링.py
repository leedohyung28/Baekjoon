def solution(n, tops):
    answer = 0
    dp = [[0] * n for _ in range(2)]
    # dp[0][n] -> not use
    # dp[1][n] -> use
    if tops[0] == 1 :
        dp[0][0] = 3
    else :
        dp[0][0] = 2
    dp[1][0] = 1
    
    for i in range(1, n) :
        if tops[i] == 1 :
            dp[0][i] = (dp[0][i-1] * 3 + dp[1][i-1] * 2) % 10007
        else :
            dp[0][i] = (dp[0][i-1] * 2 + dp[1][i-1]) % 10007
        dp[1][i] = (dp[0][i-1] + dp[1][i-1]) % 10007
    answer = (dp[0][-1] + dp[1][-1]) % 10007
    return answer