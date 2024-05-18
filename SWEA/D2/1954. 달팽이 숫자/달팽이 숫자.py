T = int(input())

for test_case in range(1, T + 1) :
    n = int(input())
    s = [[None] * n for _ in range(n)]
    
    dx = 0
    dy = 0
    num = 1
    sx = 0
    sy = 1
    ex = n-1
    ey = n-1
    
    s[0][0] = 1
    while sx <= ex and sy <= ey :
        while dx < ex :
            dx += 1
            num += 1
            s[dy][dx] = num
        ex -= 1
        
        while dy < ey :
            dy += 1
            num += 1
            s[dy][dx] = num
        ey -= 1
            
        while dx > sx :
            dx -= 1
            num += 1
            s[dy][dx] = num
        sx += 1
            
        while dy > sy :
            dy -= 1
            num += 1
            s[dy][dx] = num
        sy += 1
        
    if n % 2 != 0 :
        s[n//2][n//2] = n*n
    
    print('#'+str(test_case))
    for y in range(len(s)) :
        for x in s[y] :
            print(x, end=' ')
        print()