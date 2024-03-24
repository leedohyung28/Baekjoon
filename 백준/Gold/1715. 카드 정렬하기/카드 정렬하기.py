import sys
import heapq

N = int(sys.stdin.readline())

cards = []
for _ in range(N) :
    heapq.heappush(cards, int(sys.stdin.readline()))

result = 0
for _ in range(N-1) :
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    result += A+B
    heapq.heappush(cards, A+B)

print(result)