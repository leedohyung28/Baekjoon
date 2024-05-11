def solution(m, n, board):
    answer = 0
    changed = True
    
    while changed :
        changed = False
        ch = set()
        for y in range(m-1) :
            for x in range(n-1) :
                if board[y][x] != '_' and board[y][x] == board[y+1][x+1] == board[y][x+1] == board[y+1][x] :
                        changed = True
                        ch.add(x+y*n)
                        ch.add(x+1+y*n)
                        ch.add(x+(y+1)*n)
                        ch.add(x+1+(y+1)*n)
                        
        for i in range(m) :
            board[i] = list(board[i])

        for i in ch :
            answer += 1
            board[i//n][i%n] = '_'
        
        for x in range(n) :
            down = True
            while down :
                down = False
                for y in range(m-1) :
                    if board[y][x] != '_' and board[y+1][x] == '_' :
                        board[y+1][x] = board[y][x]
                        board[y][x] = '_'
                        down = True

        for i in range(m) :
            board[i] = ''.join(board[i])
    
    return answer