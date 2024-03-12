import sys

N = int(sys.stdin.readline())

card_prices = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N+1)
for i in range(1, N+1) :
    dp[i] = max(card_prices[i-1], dp[i])
    for j in range(1, N) :
        if i + j > N :
            break
        dp[i+j] = max(dp[i+j], dp[i]+dp[j])
        
print(dp[N])