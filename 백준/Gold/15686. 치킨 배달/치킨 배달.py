import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

m = []
for _ in range(N) :
    m.append(list(map(int, sys.stdin.readline().split())))
    
result = [[0] * 13 for _ in range(2*N)]
dx = [0,1,-1,0]
dy = [1,0,0,-1]
chicken = {}
global t
t = 0

def find(d, h) :
    global t
    vis = [[False] * N for _ in range(N)]
    vis[d[0][0]//N][d[0][0]%N] = True
    while d :
        v,k = d.popleft()
        x, y = v%N, v//N
        if m[y][x] == 2 :
            if x+y*N not in chicken :
                chicken[x+y*N] = t
                result[h][t] = k
                t += 1
            else :
                result[h][chicken[x+y*N]] = k
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not vis[ny][nx] :
                vis[ny][nx] = True
                d.append([nx+ny*N, k+1])

h = 0
for x in range(N) :
    for y in range(N) :
        if m[y][x] == 1 :
            find(deque([[x+y*N, 0]]), h)
            h += 1

answer = float('inf')
K = list(combinations(range(t), M))
for i in K :
    less = 0
    for j in range(h) :
        l = float('inf')
        for k in i :
            l = min(l, result[j][k])
        less += l
    answer = min(less, answer)
print(answer)