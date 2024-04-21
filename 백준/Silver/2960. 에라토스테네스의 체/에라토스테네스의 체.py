import sys
from math import sqrt

n, k = map(int, sys.stdin.readline().split())

tf = [True] * (n+1)

def prime(n) :
    if n == 1 :
        return False
    
    for i in range(2, int(sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

p = []
for i in range(2, n+1) :
    if prime(i) :
        p.append(i)

idx = 0
while k > 0 :
    v = p[idx]
    for i in range(v, n+1, v) :
        if tf[i] :
            tf[i] = False
            k -= 1
            if k == 0 :
                print(i)
                exit()
    idx += 1