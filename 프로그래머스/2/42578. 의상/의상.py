def solution(clothes):
    answer = 1
    c_dict = {}
    
    for i in clothes :
        if i[1] not in c_dict :
            c_dict[i[1]] = 1
        else :
            c_dict[i[1]] += 1
            
    if len(c_dict) == 1 :
        return c_dict[clothes[0][1]]
    
    else :
        for j in c_dict :
            answer *= (c_dict[j]+1)
        
    return answer - 1