import sys

N = int(sys.stdin.readline())

small = {2:1, 3:7, 4:4, 5:2, 6:0, 7:8}
    
for _ in range(N) :
    t = int(sys.stdin.readline())
    bt = t

    # small
    if t == 6 :
        print(6, end=' ')
    elif t <= 7 :
        print(small[t], end=' ')
    else :
        s = t // 7
        if t % 7 == 0 :
            print('8'*(t//7), end=' ')
        else :
            n_list = ''    
            if t <= 7*s + 2 :
                n_list += '1'
                t -= 2
                
            elif t <= 7*s + 5 :
                n_list += '2'
                t -= 5
                
            elif t <= 7*s + 4 :
                n_list += '4'
                t -= 4
            
            elif t <= 7*s + 6 :
                n_list += '6'
                t -= 6
                
            elif t <= 7*s + 3 :
                n_list += '7'
                t -= 3
                
            elif t <= 7*s + 7 :
                n_list += '8'
                t -= 7
            s -= 1
            
            while s > 0 :
                if t <= 7*s + 6 :
                    n_list += '0'
                    t -= 6
                    
                elif t <= 7*s + 2 :
                    n_list += '1'
                    t -= 2
                    
                elif t <= 7*s + 5 :
                    n_list += '2'
                    t -= 5
                    
                elif t <= 7*s + 4 :
                    n_list += '4'
                    t -= 4
                    
                elif t <= 7*s + 3 :
                    n_list += '7'
                    t -= 3
                    
                elif t <= 7*s + 7 :
                    n_list += '8'
                    t -= 7
                
                s -= 1

            n_list += str(small[t])
            if n_list[0] == '0' :
                n_list[0] = 6
            print(n_list, end=' ')
        
    # big
    if bt >= 4 :
        if bt % 2 == 0 :
            print('1'*(bt//2))
        else :
            print('7'+'1'*(bt//2-1))
    elif bt == 3 :
        print(7)
    else :
        print(1)