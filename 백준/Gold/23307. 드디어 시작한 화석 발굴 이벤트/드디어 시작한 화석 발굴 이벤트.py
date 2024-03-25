import sys

N = int(sys.stdin.readline())

g = []
for _ in range(N) :
    g.append(list(sys.stdin.readline().strip()))
    
vis = [[0] * N for _ in range(N)]
answer = []
cnt = 0

for y in range(N) :
    for x in range(N) :
        if vis[y][x] == 0 and g[y][x] == '#' :
            c = 1
            for i in range(1, N-x) :
                if g[y][x+i] == '#' and vis[y][x+i] == 0:
                    c += 1
                else :
                    break
            d = 1
            for i in range(1, N-y) :
                if g[y+i][x] == '#' and vis[y+i][x] == 0 :
                    d += 1
                else :
                    break
            if d == 1 :
                answer.append([y+c//2+1, x+c//2+1, c, 'LU'])
            elif c == 1 :
                answer.append([y+d//2+1, x+d//2+1, d, 'UL'])
            elif d-c == 2 :
                answer.append([y+d//2+1, x+d//2+1, d, 'UR'])
            elif c-d == 2 :
                answer.append([y+c//2+1, x+c//2+1, c, 'LD'])
                
            else :
                a = 1
                for i in range(1, c) :
                    if g[y+i][x+c-1] == '#' and vis[y+i][x+c-1] == 0 :
                        a += 1
                    else :
                        break   
                b = 1
                for i in range(1, d) :
                    if g[y+d-1][x+i] == '#' and vis[y+d-1][x+i] == 0 :
                        b += 1
                    else :
                        break
                if a == 1 :
                    answer.append([y+c//2+1, x+c//2+1, c, 'RU'])              
                elif b == 1 :
                    answer.append([y+d//2+1, x+d//2+1, d, 'DL'])
                elif a-b == 2 :
                    answer.append([y+c//2+1, x+c//2+1, c, 'DR'])
                elif b-a == 2 :
                    answer.append([y+d//2+1, x+d//2+1, d, 'RD'])
                    
            for k in range(max(c,d)) :
                for j in range(max(c,d)) :
                    vis[y+k][x+j] = 1
            cnt += 1

print(cnt)
answer.sort(key = lambda x: (x[0], x[1]))
for i in answer :
    print(i[0], i[1], i[2], i[3])