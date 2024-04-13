import sys

n, k = map(int, sys.stdin.readline().split())

w = []
b = []
for _ in range(n) :
    t1, p1, t2, p2 = map(int, sys.stdin.readline().split())
    w.append([t1, p1])
    b.append([t2, p2])

d = [[0]*(k+1) for _ in range(n)]
d[0][k-w[0][0]] = w[0][1]
d[0][k-b[0][0]] = b[0][1]

for i in range(n-1) :
    for j in range(k) :
        if d[i][j] != 0 and j >= w[i+1][0] :
            d[i+1][j-w[i+1][0]] = max(d[i][j] + w[i+1][1], d[i+1][j-w[i+1][0]])
            
        if d[i][j] != 0 and j >= b[i+1][0] :
            d[i+1][j-b[i+1][0]] = max(d[i][j] + b[i+1][1], d[i+1][j-b[i+1][0]])
    k -= min(w[i+1][0], b[i+1][0])
print(max(d[-1]))