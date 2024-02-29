import sys

n = int(sys.stdin.readline())

a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

parent_num = [[False] * n for _ in range(n)]
for _ in range(m) :
    p, s = map(int, sys.stdin.readline().split())
    parent_num[p-1][s-1] = True
    parent_num[s-1][p-1] = True

chon = [-1] * n
visited = [False] * n

def dfs(a) :
    visited[a-1] = True
    for i in range(n) :
        if parent_num[a-1][i] and visited[i] is False:
            visited[i] = True
            chon[i] = chon[a-1] + 1
            dfs(i+1)
            
chon[a-1] = 0
dfs(a)
print(chon[b-1])