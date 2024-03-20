def solution(today, terms, privacies):
    answer = []

    def compare(today, date, bt) :
        ty, tm, td = today.split(".")
        dy, dm, dd = date.split(".")
        
        if int(ty) > int(dy) :
            tm = (int(ty)-int(dy))*12 + int(tm)
        if int(tm) - int(dm) > bt : return True
        elif int(tm) - int(dm) == bt :
            if int(td) >= int(dd) : return True
            else : return False
        else : return False
    
    for i in range(len(privacies)) :
        date, a  = privacies[i].split()
        
        for k in terms :
            t, n = k.split()
            
            if t == a :
                tf = compare(today, date, int(n))
                if tf :
                    answer.append(i+1)
                break
    
    return answer