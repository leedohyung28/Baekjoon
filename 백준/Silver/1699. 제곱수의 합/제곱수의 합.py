import sys
import math

N = int(sys.stdin.readline())

dp = [i for i in range(N+1)]

for k in range(1, N+1) :
    if math.sqrt(k) % 1 == 0 :
        dp[k] = 1
    else :
        for j in range(1, k) :
            if j*j > k :
                break
            if dp[k] > dp[k-j*j] + dp[j*j] :
                dp[k] = dp[k-j*j] + dp[j*j]

print(dp[N])