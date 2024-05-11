from collections import deque

def solution(dartResult):
    answer = 0
    
    d = deque()
    
    for i in range(len(dartResult)) :
        if dartResult[i] == 'S' :
            if len(d) == 2 :
                answer += d.popleft()
            if i > 1 and dartResult[i-2] == '1' :
                d.append(10)
            else :
                d.append(int(dartResult[i-1]))
        
        elif dartResult[i] == 'D' :
            if len(d) == 2 :
                answer += d.popleft()
            if i > 1 and dartResult[i-2] == '1' :
                d.append(100)
            else :
                d.append(int(dartResult[i-1])**2)
            
        elif dartResult[i] == 'T' :
            if len(d) == 2 :
                answer += d.popleft()
            if i > 1 and dartResult[i-2] == '1' :
                d.append(1000)
            else :
                d.append(int(dartResult[i-1])**3)
            
        elif dartResult[i] == '#' :
            if len(d) > 0 :
                d[-1] = d[-1]*-1
            
        elif dartResult[i] == '*' :
            if len(d) > 0 :
                for i in range(len(d)) :
                    d[i] = d[i]*2
    
    for i in d :
        answer += i
    
    return answer