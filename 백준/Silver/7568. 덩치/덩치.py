import sys

N = int(sys.stdin.readline())

heights = []
weights = []
for _ in range(N) :
    h,w = map(int, sys.stdin.readline().split())
    heights.append(h)
    weights.append(w)
    
bigger = [1] * N
for i in range(N-1) :
    for j in range(i+1, N) :
        if heights[i] > heights[j] and weights[i] > weights[j] :
            bigger[j] += 1
        elif heights[j] > heights[i] and weights[j] > weights[i] :
            bigger[i] += 1
            
for k in bigger :
    print(k, end=' ')