import sys
from math import ceil

N, H = map(int, sys.stdin.readline().split())

s = []
for _ in range(N) :
    t, a, h = map(int, sys.stdin.readline().split())
    if t == 2 :
        H += a
    s.append([t,a,h])
    
hp = 1
result = 0
for i in range(len(s)-1, -1, -1) :
    if s[i][0] == 1 :
        hp += (ceil(s[i][2]/H)-1) * s[i][1]
        result = max(result, hp)
    else :
        hp -= s[i][2]
        H -= s[i][1]
        if hp < 1 :
            hp = 1
            
print(result)