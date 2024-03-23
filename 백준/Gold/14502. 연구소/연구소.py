import sys
from collections import deque
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

m = []
for _ in range(N) :
    m.append(list(map(int, sys.stdin.readline().split())))
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def virus(m, d) :
    vis = [[0] * M for _ in range(N)]
    v_num = 0

    while d :
        v_num += 1
        [x,y] = d.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and vis[ny][nx] == 0 and m[ny][nx] == 0 :
                vis[ny][nx] = 1
                d.append([nx,ny])
    
    return v_num

result = float('inf')
woods = []
wall = 0
deq = deque()

for x in range(M) :
    for y in range(N) :
        if m[y][x] == 0 :
            woods.append(x+y*M)
        elif m[y][x] == 2 :
            deq.append([x,y])
        else :
            wall += 1

for a, b, c in combinations(woods, 3) :
    m[a//M][a%M] = 1
    m[b//M][b%M] = 1
    m[c//M][c%M] = 1
    result = min(result, virus(m, deq.copy()))
    m[a//M][a%M] = 0
    m[b//M][b%M] = 0
    m[c//M][c%M] = 0

print(N*M-wall-result-3)