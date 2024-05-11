def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n) :
        a = ""
        for k in range(n-1, -1, -1) :
            sharp = False
            if arr1[i] >= 2**k :
                arr1[i] -= 2**k
                sharp = True
            
            if arr2[i] >= 2**k :
                arr2[i] -= 2**k
                sharp = True
                
            if sharp :
                a += "#"
            else :
                a += " "
        
        answer.append(a)
    
    return answer
