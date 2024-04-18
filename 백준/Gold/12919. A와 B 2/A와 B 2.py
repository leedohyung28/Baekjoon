import sys
from collections import deque

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
T = len(t)
S = len(s)

q = deque([s])
while q :
    v = q.popleft()
    l = len(v)

    if l == T :
        if v == t :
            print(1)
            exit()

    else :
        a = v+'A'
        for i in range(T-l) :
            if t[i:i+l+1] == a or t[i:i+l+1] == a[::-1]:
                q.append(a)
                break

        b = v+'B'
        for i in range(T-l) :
            if t[i:i+l+1] == b or t[i:i+l+1] == b[::-1]:
                q.append(b[::-1])
                break

print(0)