import sys

K, N = map(int, sys.stdin.readline().split())

line_lists = []
for _ in range(K) :
    line_lists.append(int(sys.stdin.readline()))
    
result = min(line_lists)
at_least = 0
at_most = max(line_lists)

while True :
    num = 0
    num2 = 0
    result_plus1 = result + 1
    for i in range(K) :
        num += line_lists[i] // result
        num2 += line_lists[i] // result_plus1
    if num == N and num2 != N :
        print(result)
        exit()
    elif num < N :
        at_most = result
    else :
        if at_least == result :
            print(result)
            exit()
        at_least = result
    result = (at_least + at_most) // 2