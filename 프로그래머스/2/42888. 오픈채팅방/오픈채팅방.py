def solution(record):
    answer = []
    
    d = dict()
    l = []
    for i in record :
        if i[0] == 'L' :
            a,b = i.split(' ')
            l.append([False, b])
        else :
            a,b,c = i.split(' ')
            if a[0] == 'E' :
                l.append([True, b])
            
            d[b] = c
    
    for i in l :
        if i[0] :
            msg = d[i[1]] + "님이 들어왔습니다."
        else :
            msg = d[i[1]] + "님이 나갔습니다."
        answer.append(msg)
    
    return answer