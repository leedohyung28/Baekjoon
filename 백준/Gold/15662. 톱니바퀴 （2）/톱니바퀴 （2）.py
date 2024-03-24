import sys
from collections import deque

T = int(sys.stdin.readline())

w = []
for _ in range(T) :
    w.append(list(map(int, sys.stdin.readline().strip())))
    
top = [0] * T

K = int(sys.stdin.readline())
for _ in range(K) :
    N, LR = map(int, sys.stdin.readline().split())
    d = deque([[N, LR]])
    vis = [False] * T
    while d :
        [v, LR] = d.popleft()
        vis[v-1] = True
        if v < T and vis[v] is False and w[v-1][(top[v-1]+2)%8] != w[v][(top[v]+6)%8] :
            d.append([v+1, -LR])
        
        if v > 1 and vis[v-2] is False and w[v-1][(top[v-1]+6)%8] != w[v-2][(top[v-2]+2)%8] :
            d.append([v-1, -LR])
            
        top[v-1] = (top[v-1] - LR + 8) % 8

result = 0
for i in range(T) :
    if w[i][top[i]] == 1 :
        result += 1
print(result)