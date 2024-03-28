import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

con = [[False] * N for _ in range(N)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    con[a-1][b-1] = True
    
answer = 0
for i in range(N) :
    u = deque([i])
    d = deque([i])
    vis = [False] * N
    vis[i] = True
    q = 1
    while u :
        v = u.popleft()
        for i in range(N) :
            if con[v][i] and not vis[i] :
                u.append(i)
                vis[i] = True
                q += 1
    while d :
        w = d.popleft()
        for k in range(N) :
            if con[k][w] and not vis[k] :
                d.append(k)
                vis[k] = True
                q += 1
            
    if q == N :
        answer += 1

print(answer)