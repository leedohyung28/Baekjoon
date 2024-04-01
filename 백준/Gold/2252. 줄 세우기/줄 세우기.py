import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

v = [0] * (N+1)
h2t = {}

for _ in range(M) :
    h, t = map(int, sys.stdin.readline().split())
    v[t] += 1
    
    if h not in h2t :
        h2t[h] = [t]
    else :
        h2t[h].append(t)

def ts(i) :
    if v[i] == 0 :
        print(i, end=' ')
        v[i] -= 1
        if i in h2t :
            for j in h2t[i] :
                v[j] -= 1
                ts(j)

for i in range(1, N+1) :
    ts(i)