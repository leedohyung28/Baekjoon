import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())


if n > k :
    print(n-k)
    for i in range(n, k-1, -1) :
        print(i, end=' ')

else :
    dp = [float('inf')] * (200_000)
    dp[n] = 0
    q = deque([[n, str(n)]])
    while q :
        v, s = q.popleft()

        if v == k :
            print(dp[v])
            print(s)
            exit()

        if v < k :
            if dp[2*v] > dp[v] + 1 :
                dp[2*v] = dp[v] + 1
                q.append([2*v, s+' '+str(2*v)])
        
            if dp[v+1] > dp[v] + 1 :
                dp[v+1] = dp[v] + 1
                q.append([v+1, s+' '+str(v+1)])

        if v > 0 and dp[v-1] > dp[v] + 1 :
            dp[v-1] = dp[v] + 1
            q.append([v-1, s+' '+str(v-1)])