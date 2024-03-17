import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dp = [float('inf')] * 200_001

q = deque([[N, 0]])

while q :
    v = q.popleft()
    loc, count = v[0], v[1]
    if 0 <= loc < 200_000 and dp[loc] > count :
        dp[loc] = count
        if count < dp[K] :
            if loc < K :
                q.append([loc*2, count+1])
                q.append([loc+1, count+1])
            q.append([loc-1, count+1])

print(dp[K])