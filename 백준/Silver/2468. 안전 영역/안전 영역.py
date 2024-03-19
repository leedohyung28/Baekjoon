import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

areas = []
for _ in range(N) :
    areas.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def find(x, y, visited) :
    visited[y][x] = True

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] is False and areas[ny][nx] > rain :
            find(nx, ny, visited)

rain = 0
max_area = 0
while rain <= 100 :
    area = 0
    visited = [[False] * N for _ in range(N)]

    for y in range(N) :
        for x in range(N) :
            if visited[y][x] is False and areas[y][x] > rain :
                find(x, y, visited)
                area += 1
    
    if area == 0 :
        break
    
    if max_area <= area :
        max_area = area

    rain += 1

print(max_area)