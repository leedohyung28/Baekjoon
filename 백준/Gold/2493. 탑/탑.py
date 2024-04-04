import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

stack = [[T[0], 1]]
print(0, end=' ')
for i in range(1, len(T)) :
    while stack :
        h, idx = stack[-1]
        if h <= T[i] :
            stack.pop()
        else :
            print(idx, end=' ')
            stack.append([T[i], i+1])
            b = True
            break
    if not stack :
        print(0, end=' ')
        stack.append([T[i], i+1])