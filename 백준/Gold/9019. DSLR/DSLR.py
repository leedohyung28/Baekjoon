import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T) :
    s, e = map(int, sys.stdin.readline().split())
    d = deque([s])
    
    n = [''] * 10_000
    vis = [False] * 10_000
    
    while d :
        v = d.popleft()
        
        if v != v*2%10_000 and not vis[v*2%10_000] :
            vis[v*2%10_000] = True
            n[v*2%10_000] = n[v] + 'D'
            if v*2%10_000 == e :
                print(n[v*2%10_000])
                break
            d.append(v*2%10_000)
        
        if v == 0 and not vis[9999] :
            vis[9999] = True
            n[9999] = n[0] + 'S'
            if 9999 == e :
                print(n[9999])
                break
            d.append(9999)
        elif not vis[v-1] :
            vis[v-1] = True
            n[v-1] = n[v] + 'S'
            if v-1 == e :
                print(n[v-1])
                break
            d.append(v-1)

        l = (v // 1000) + (v % 1000) * 10
        if not vis[l] :
            vis[l] = True
            n[l] = n[v] + 'L'
            if l == e :
                print(n[l])
                break
            d.append(l)

        r = (v % 10) * 1000 + v // 10
        if not vis[r] :
            vis[r] = True
            n[r] = n[v] + 'R'
            if r == e :
                print(n[r])
                break
            d.append(r)