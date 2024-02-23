import sys

H, W = map(int, sys.stdin.readline().split())

cloud_map = []

for _ in range(H) :
    cloud_map.append(list(sys.stdin.readline().rstrip()))


for i in range(H) :
    time = 0
    cloud_coming = False
    for k in range(W) :        
        if cloud_map[i][k] == 'c' :
            time = 0
            print(time, end=' ')
            cloud_coming = True
        
        elif cloud_coming is True :
            time += 1
            print(time, end=' ')
        
        else :
            print(-1, end=' ')
    print()