import sys

tc = int(sys.stdin.readline())

def union(a,b) :
    a = find(a)
    b = find(b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

for t in range(tc) :
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    
    parent = [i for i in range(n)]
    
    for _ in range(k) :
        a, b = map(int, sys.stdin.readline().split())
        union(a,b)
        
    m = int(sys.stdin.readline())

    print('Scenario ', t+1, ':', sep='')
    for _ in range(m) :
        u, v = map(int, sys.stdin.readline().split())
        if find(u) == find(v) :
            print(1)
        else :
            print(0)
    print()