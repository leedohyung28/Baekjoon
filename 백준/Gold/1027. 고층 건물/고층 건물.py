import sys

N = int(sys.stdin.readline())

if N == 1 :
    a = sys.stdin.readline().strip()
    print(0)
    exit()
    
t = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N) :
    result = 0
    for j in range(N) :
        if i < j :
            result += 1
            st = (t[j] - t[i]) / (j - i)
            for k in range(i+1, j) :
                if (t[k] - t[i]) / (k - i) >= st :
                    result -= 1
                    break
        elif i > j :
            result += 1
            st = (t[i] - t[j]) / (i - j)
            for k in range(j+1, i) :
                if (t[k] - t[j]) / (k - j) >= st :
                    result -= 1
                    break
    answer = max(result, answer)
    
print(answer)