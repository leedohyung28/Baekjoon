import sys

N = int(sys.stdin.readline())
s = []

result = 0
for _ in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    while s :
        h = s.pop()
        if h < y :
            s.append(h)
            s.append(y)
            result += 1
            break
        elif h == y :
            s.append(h)    
            break
            
    if len(s) == 0 :
        if y > 0 :
            s.append(y)
            result += 1
        
print(result)