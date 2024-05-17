def solution(words):
    words.sort()
    
    answer = 0
    
    g = False
    for j in range(min(len(words[0]), len(words[1]))) :
        if words[0][j] != words[1][j] :
            answer = j+1
            last = words[0][:j+1]
            g = True
            break
    if not g :
        if len(words[0]) > len(words[1]) :
            answer = len(words[1]) + 1
            last = words[0][:len(words[1])+1]
        else :
            answer = len(words[0])
            last = words[0]
    
    for i in range(1, len(words)-1) :
        l = False
        r = False
        g = False
        for j in range(len(words[i])) :
            if not l and j < len(last) :
                if last[j] != words[i][j] :
                    l = True
                
            if not r and j < len(words[i+1]) :
                if words[i+1][j] != words[i][j] :
                    r = True
            
            if l and r :
                last = words[i][:j+1]
                answer += j+1
                g = True
                break
                
            if j == len(last)-1 :
                    l = True
            if j == len(words[i+1])-1 :
                    r = True
        if not g :
            last = words[i]
            answer += len(words[i])
            
    g = False
    for j in range(min(len(words[-1]), len(last))) :
        if words[-1][j] != last[j] :
            answer += j+1
            g = True
            break
    if not g :
        if len(words[-1]) > len(last) :
            answer += len(last) + 1
        else :
            answer += len(words[-1])
    
    return answer