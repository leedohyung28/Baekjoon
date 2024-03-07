import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * (K+1) for _ in range(N+1)]

W = []
V = []

for _ in range(N) :
    w, v = map(int, sys.stdin.readline().split())
    W.append(w)
    V.append(v)
    
for i in range(1, N+1) :
    for j in range(1, K+1) :
        if W[i-1] <= j :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]]+V[i-1])
        else :
            dp[i][j] = dp[i-1][j]

print(max(dp[N]))