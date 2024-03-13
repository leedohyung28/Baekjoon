import sys, heapq

N = int(sys.stdin.readline())

numbers = []
for _ in range(N) :
    input = int(sys.stdin.readline())
    if input == 0 :
        if len(numbers) == 0 :
            print(0)
        else :
            print(heapq.heappop(numbers))
    else :
        heapq.heappush(numbers, input)