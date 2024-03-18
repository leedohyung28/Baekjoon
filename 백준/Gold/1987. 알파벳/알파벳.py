import sys

R, C = map(int, sys.stdin.readline().split())

board = []
for _ in range(R) :
    board.append(list(sys.stdin.readline().strip()))
    
cross = [[0] * C for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, count, alpha) :
    cross[y][x] = max(cross[y][x], count)
    alpha.add(board[y][x])
    
    for k in range(4) :
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx <= C-1 and 0 <= ny <= R-1 and board[ny][nx] not in alpha :
            move(nx, ny, count+1, alpha)

    alpha.remove(board[y][x])

        
move(0, 0, 1, set())

result = 0
for i in range(R) :
    result = max(result, max(cross[i]))
print(result)