import sys

n = int(sys.stdin.readline())

longest = 0
total = 0

x, y = 0, 0
bx, by = 0 , 0
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    if i == 0 :
        x, y = a, b
        bx, by = a, b
    else :
        dis = abs(x-a) + abs(y-b)
        total += dis
        if i > 1 :
            ddis = abs(bx-a) + abs(by-b)
            if longest < dis + bdis - ddis :
                longest = dis + bdis - ddis
        bdis = dis
        bx, by = x, y
        x, y = a, b
        
print(total-longest)