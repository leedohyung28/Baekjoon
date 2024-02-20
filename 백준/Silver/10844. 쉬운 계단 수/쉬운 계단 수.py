import sys
N = int(sys.stdin.readline())

if N == 1 :
    print(9)
elif N == 2 :
    print(17)
else :
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for k in range(N-1) :
        new_dp = [0] * 10
        for i in range(10) :
            if i == 0 :
                new_dp[0] = dp[1]
            elif i == 9 :
                new_dp[9] = dp[8]
            else :
                new_dp[i] += dp[i-1] + dp[i+1]
        dp = new_dp.copy()
    print(sum(dp)%1_000_000_000)