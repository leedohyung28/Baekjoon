def solution(files):
    answer = []
    seperated = []
    
    for i in files :
        head = ''
        number = ''
        tail = ''
        h = False
        n = False
        h_stop = 0
        for j in range(len(i)) :
            if not h and i[j].isnumeric() :
                head += i[:j]
                h_stop = j
                h = True
            
            elif h and not i[j].isnumeric() :
                number += i[h_stop:j]
                tail += i[j:]
                n = True
                break

        if not h :
            head += i
        elif not n :
            number += i[h_stop:]
        seperated.append([head, number, tail])

    seperated.sort(key=lambda x:(x[0].lower(),int(x[1])))

    
    for a,b,c in seperated :
        answer.append(a+str(b)+c)

    return answer