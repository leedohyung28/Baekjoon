import sys

n = int(sys.stdin.readline())
m = list(sys.stdin.readline().strip())

s = 'E'
result = 0
for i in range(n) :
    if m[i] != s :
        if s == 'E' :
            result += 1
        s = m[i]
        
if s[-1] == 'E' :
    result += 1
        
print(result)