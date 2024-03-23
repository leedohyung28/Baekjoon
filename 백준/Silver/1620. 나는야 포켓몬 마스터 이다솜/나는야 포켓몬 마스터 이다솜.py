import sys

N, M = map(int, sys.stdin.readline().split())

pmon = {}
pmon2 = {}
n = 1
for _ in range(N) :
    p = sys.stdin.readline().strip()
    pmon[p] = n
    pmon2[n] = p
    n += 1
    
num = ['0','1','2','3','4','5','6','7','8','9']
for _ in range(M) :
    i = sys.stdin.readline().strip()
    
    if i[0] in num :
        print(pmon2[int(i)])
    else :
        print(pmon[i])