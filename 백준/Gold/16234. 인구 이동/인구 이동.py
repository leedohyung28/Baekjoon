import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

m = []
for _ in range(n) :
    m.append(list(map(int, sys.stdin.readline().split())))

c = True
cnt = -1
dx = [1,0,0,-1]
dy = [0,1,-1,0]

while c :
    c = False
    cnt += 1
    v = [[False] * n for _ in range(n)]
    for x in range(n) :
        for y in range(n) :
            if not v[y][x] :
                d = deque([[x,y]])
                d_list = [[x,y]]
                total = 0
                v[y][x] = True
                while d :
                    ix,iy = d.popleft()
                    total += m[iy][ix]
                    for i in range(4) :
                        nx = ix + dx[i]
                        ny = iy + dy[i]
                        if 0 <= nx < n and 0 <= ny < n and not v[ny][nx] and l <= abs(m[ny][nx] - m[iy][ix]) <= r :
                            c = True
                            v[ny][nx] = True
                            d_list.append([nx,ny])
                            d.append([nx,ny])

                s_total = total // len(d_list)
                for i in d_list :
                    m[i[1]][i[0]] = s_total     

print(cnt)