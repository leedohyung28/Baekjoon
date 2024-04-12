import sys
from collections import deque

dx = [0,1,-1,0]
dy = [1,0,0,-1]
tc = 1

while True :
    N = int(sys.stdin.readline())
    
    if N == 0 :
        break
    
    C = []
    for _ in range(N) :
        C.append(list(map(int, sys.stdin.readline().split())))
        
    A = [[float('inf')] * N for _ in range(N)]
    A[0][0] = C[0][0]
    v = deque([[0,0]])
    
    while v :
        x,y = v.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and A[ny][nx] > C[ny][nx] + A[y][x] :
                A[ny][nx] = C[ny][nx] + A[y][x]
                v.append([nx,ny])
    print(f'Problem {tc}:', A[-1][-1])
    tc += 1