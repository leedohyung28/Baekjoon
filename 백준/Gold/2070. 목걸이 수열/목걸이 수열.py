S = list(input())
    
list1 = []

a = ''
for i in S :
    if len(a) == 0 or i == '1' :
        a += i
    elif a[-1] == '0' :
        a += i
    else :
        list1.append(a)
        a = i
list1.append(a)
        
if len(list1) == 1 :
    print('(%s)' % list1[0])

else :
    
    def necklace(N) :
        std = N
        for i in range(1, len(N)+1) :
            cmp = N[i:] + N[:i]
            if int(std) > int(cmp) :
                return False
        return True

    while True :
        list1.reverse()
        list2 = []
        Q = len(list1)
        
        while len(list1) > 1 :
            A = list1.pop()
            B = list1.pop()
            if necklace(A+B) :
                list1.append(A+B)
            
            else :
                list2.append(A)
                list1.append(B)
        
        list2.append(list1.pop())
        if len(list2) == Q :
            break
        else :
            list1 = list2.copy()
            continue
        
    for i in range(len(list2)) :
        print('(%s)' % list2[i], end='')