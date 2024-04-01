import sys
from collections import deque

iA, iB, fA, fB = map(int, sys.stdin.readline().split())

dp = [[float('inf')] * (iB+1) for _ in range(iA+1)]
dp[0][0] = 0
q = deque([[0,0,0]])

while q :
    a,b,k = q.popleft()
    if a != iA and dp[iA][b] > k:
        dp[iA][b] = min(dp[iA][b], k+1)
        q.append([iA, b, k+1])
    if b != iB and dp[a][iB] > k :
        dp[a][iB] = min(dp[a][iB], k+1)
        q.append([a, iB, k+1])
    
    if a != 0 :
        if dp[0][b] > k :
            dp[0][b] = min(dp[0][b], k+1)
            q.append([0, b, k+1])
        if a+b < iB and dp[0][a+b] > k :
            dp[0][a+b] = min(dp[0][a+b], k+1)
            q.append([0,a+b,k+1])
        if a+b > iB and dp[a+b-iB][iB] > k :
            dp[a+b-iB][iB] = min(dp[a+b-iB][iB], k+1)
            q.append([a+b-iB,iB,k+1])
        
    if b != 0 :
        if dp[a][0] > k :
            dp[a][0] = min(dp[a][0], k+1)
            q.append([a, 0, k+1])
        if a+b < iA and dp[a+b][0] > k :
            dp[a+b][0] = min(dp[a+b][0], k+1)
            q.append([a+b,0,k+1])
        if a+b > iA and dp[iA][a+b-iA] > k :
            dp[iA][a+b-iA] = min(dp[iA][a+b-iA], k+1)
            q.append([iA,a+b-iA,k+1])

print(dp[fA][fB] if dp[fA][fB] != float('inf') else -1)