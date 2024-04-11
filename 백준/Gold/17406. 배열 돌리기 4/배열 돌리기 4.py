import sys
from collections import deque
from itertools import permutations
import copy

N, M, K = map(int, sys.stdin.readline().split())

A = []
for _ in range(N) :
    A.append(list(map(int, sys.stdin.readline().split())))
    
C = []
for _ in range(K) :
    C.append(list(map(int, sys.stdin.readline().split())))
  
P = list(permutations([x for x in range(K)], K))

result = float('inf')
for idx in P :
    tmp_map = copy.deepcopy(A)
    for k in list(idx) :
        r, c, s = C[k]
        
        x_start = c-s-1
        y_start = r-s-1
        x_end = c+s-1
        y_end = r+s-1
        
        while x_start < x_end and y_start < y_end :
            x = x_start
            y = y_start
            D = deque([tmp_map[y_start][x_start]])
            while x != x_end :
                x += 1
                D.append(tmp_map[y][x])
                tmp_map[y][x] = D.popleft()
            while y != y_end :
                y += 1
                D.append(tmp_map[y][x])
                tmp_map[y][x] = D.popleft()
            while x != x_start :
                x -= 1
                D.append(tmp_map[y][x])
                tmp_map[y][x] = D.popleft()
            while y != y_start :
                y -= 1
                D.append(tmp_map[y][x])
                tmp_map[y][x] = D.popleft()
            
            x_start += 1
            y_start += 1
            x_end -= 1
            y_end -= 1
    for i in range(N) :
        result = min(result, sum(tmp_map[i]))
print(result)