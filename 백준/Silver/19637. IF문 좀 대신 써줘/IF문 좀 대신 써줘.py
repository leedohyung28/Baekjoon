import sys

N, M = map(int, sys.stdin.readline().split())

names = []
ranges = []
for _ in range(N) :
    n, r = sys.stdin.readline().split()
    r = int(r)
    names.append(n)
    ranges.append(r)
                
for _ in range(M) :
    num = int(sys.stdin.readline())
    
    top, bot = N-1, 0
    result = 0
    
    while bot <= top :
        mid = (top + bot) // 2
        
        if num > ranges[mid] :
            bot = mid + 1
            continue
        
        else :
            result = mid
            top = mid - 1
            
    print(names[result])