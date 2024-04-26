def solution(rows, columns, queries):
    
    m = []
    for r in range(rows) :
        tmp = []
        for c in range(columns) :
            tmp.append(c+r*columns+1)
        m.append(tmp)
    answer = []
    
    for q in queries :
        y1, x1, y2, x2 = q
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
        
        k = 0
        x1_init = x1
        y1_init = y1
        mn = 10_001
        
        while x1 < x2 :
            t = m[y1][x1]
            mn = min(t, mn)

            m[y1][x1] = k
            k = t
            x1 += 1
            
        while y1 < y2 :
            t = m[y1][x1]
            mn = min(t, mn)
            m[y1][x1] = k
            k = t
            y1 += 1
    
        while x2 > x1_init :
            t = m[y2][x2]
            mn = min(t, mn)
            m[y2][x2] = k
            k = t
            x2 -= 1
            
        while y2 > y1_init :
            t = m[y2][x2]
            mn = min(t, mn)
            m[y2][x2] = k
            k = t
            y2 -= 1
        m[y2][x2] = t
        answer.append(mn)
            
    return answer