def solution(maze):    

    global H
    global W
    global answer
    
    H = len(maze)
    W = len(maze[0])
    bm = [[False] * W for _ in range(H)]
    rm = [[False] * W for _ in range(H)]
    
    for y in range(H) :
        for x in range(W) :
            if maze[y][x] == 2 :
                bx = x
                by = y
            elif maze[y][x] == 1 :
                rx = x
                ry = y
            elif maze[y][x] == 5 :
                bm[y][x] = True
                rm[y][x] = True

    bm[by][bx] = True
    rm[ry][rx] = True
    
    answer = H*W+1
    move(bx,by,bm,rx,ry,rm,0,maze)
    
    if answer == H*W+1 :
        return 0
    else :
        return answer
    
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def move(bx,by,bm,rx,ry,rm,k,maze) :
    global answer
    
    if maze[by][bx] != 4 :
        for i in range(4) :
            nbx = bx + dx[i]
            nby = by + dy[i]

            if 0 <= nbx < W and 0 <= nby < H and not bm[nby][nbx] :
                bm[nby][nbx] = True
                if maze[ry][rx] != 3 :
                    for q in range(4) :
                        nrx = rx + dx[q]
                        nry = ry + dy[q]
                        if 0 <= nrx < W and 0 <= nry < H and not rm[nry][nrx] and not (nrx==nbx and nry==nby) and not(nrx==bx and nry==by and nbx==rx and nby==ry) :
                            rm[nry][nrx] = True
                            a = move(nbx,nby,bm,nrx,nry,rm,k+1,maze)
                            if a :
                                answer = min(answer,a)
                            
                            rm[nry][nrx] = False
                elif not (nbx==rx and nby==ry)  :
                    a = move(nbx,nby,bm,rx,ry,rm,k+1,maze)
                    if a :
                        answer = min(answer,a)
                    
                bm[nby][nbx] = False

    elif maze[ry][rx] != 3 :
        for j in range(4) :
            nrx = rx + dx[j]
            nry = ry + dy[j]
            if 0 <= nrx < W and 0 <= nry < H and not rm[nry][nrx] and not (nry == by and nrx == bx) :
                rm[nry][nrx] = True
                a = move(bx,by,bm,nrx,nry,rm,k+1,maze)
                if a :
                    answer = min(answer,a)
                rm[nry][nrx] = False
            
    else :
        return k