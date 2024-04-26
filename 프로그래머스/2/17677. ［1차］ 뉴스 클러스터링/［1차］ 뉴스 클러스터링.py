def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    list1 = {}
    list2 = {}
    
    for i in range(len(str1)-1) :
        if str1[i].isalpha() and str1[i+1].isalpha() :
            if str1[i:i+2] not in list1 :
                list1[str1[i:i+2]] = 0
            list1[str1[i:i+2]] += 1
    
    for i in range(len(str2)-1) :
        if str2[i].isalpha() and str2[i+1].isalpha() :
            if str2[i:i+2] not in list2 :
                list2[str2[i:i+2]] = 0
            list2[str2[i:i+2]] += 1
    
    gyo = 0
    hap = 0
    
    for i in list1.keys() :
        if i in list2 :
            gyo += min(list2[i], list1[i])
            hap += max(list2[i], list1[i])
        else :
            hap += list1[i]
    
    for j in list2.keys() :
        if j not in list1 :
            hap += list2[j]

    if hap == 0 :
        answer = 65536
    else :
        answer = int(gyo/hap*65536)
    
    return answer