def solution(line):
    answer = []
    N = len(line)
    points = []
    
    maxX = -float('inf')
    minX = float('inf')
    maxY = -float('inf')
    minY = float('inf')
    for m in range(N-1) :
        for n in range(m+1, N) :
            a = line[m][0]
            b = line[m][1]
            e = line[m][2]
            c = line[n][0]
            d = line[n][1]
            f = line[n][2]
            
            if a*d-b*c != 0 :
                X = (b*f-e*d)/(a*d-b*c)
                Y = (e*c-a*f)/(a*d-b*c)
            
            if X % 1 == 0 and Y % 1 == 0 :
                if X > maxX :
                    maxX = int(X)
                if X < minX :
                    minX = int(X)
                if Y > maxY :
                    maxY = int(Y)
                if Y < minY :
                    minY = int(Y)
                
                points.append([int(X), int(Y)])
    
    for y in range(maxY, minY-1, -1) :
        stars = ''
        for x in range(minX, maxX+1) :
            if [x,y] in points :
                stars += '*'
            else :
                stars += '.'
        answer.append(stars)
    
    
    return answer