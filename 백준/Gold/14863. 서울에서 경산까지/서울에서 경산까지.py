import sys

n, k = map(int, sys.stdin.readline().split())

w = []
b = []
for _ in range(n) :
    t1, p1, t2, p2 = map(int, sys.stdin.readline().split())
    w.append([t1, p1])
    b.append([t2, p2])

result = 0
def go(i,k,total) :
    global result
    if i == n :
        result = max(total,result)
    else :
        if k >= w[i][0] :
            go(i+1,k-w[i][0], total+w[i][1])
        if k >= b[i][0] :
            go(i+1,k-b[i][0], total+b[i][1])
            
go(0,k,0)
print(result)