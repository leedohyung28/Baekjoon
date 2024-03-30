import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

m = []

for _ in range(N) :
    m.append(list(map(int, sys.stdin.readline().strip())))
    
w = [[float('inf')] * M for _ in range(N)]
d = deque([[0,0,1]])
dx = [0,1,-1,0]
dy = [1,0,0,-1]

w[0][0] = 1
while d :
    x,y,k = d.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and m[ny][nx] == 0  and w[ny][nx] > k+1 :
            w[ny][nx] = k+1
            d.append([nx,ny,k+1])
    
z = [[float('inf')] * M for _ in range(N)]
d = deque([[M-1,N-1,1]])

z[N-1][M-1] = 1
while d :
    x,y,k = d.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and m[ny][nx] == 0 and z[ny][nx] > k+1 :
            z[ny][nx] = k+1
            d.append([nx,ny,k+1])

result = float('inf')
for x in range(M) :
    for y in range(N) :
        if m[y][x] == 1 :
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and w[ny][nx] != float('inf') :
                    for k in range(4) :
                        if k != i :
                            kx = x + dx[k]
                            ky = y + dy[k]
                            if 0 <= kx < M and 0 <= ky < N and z[ky][kx] != float('inf') :
                                result = min(result, w[ny][nx] + z[ky][kx] + 1)                

result = min(result, z[0][0], w[N-1][M-1])               
if result == float('inf') :
    print(-1)
else :
    print(result)