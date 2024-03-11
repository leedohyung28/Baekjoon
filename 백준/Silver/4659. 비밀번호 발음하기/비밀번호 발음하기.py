import sys

while True :
    input = sys.stdin.readline().strip()
    if input == 'end' :
        break
    
    N = len(input)
    vowels = ['a', 'e', 'i', 'o', 'u']
    passed = False
    
    if N == 1 :
        if input in vowels :
            print('<',input,'> is acceptable.', sep='')
        else :
            print('<',input,'> is not acceptable.', sep='')
    elif N == 2 :
        if input[0] in vowels or input[1] in vowels :
            if input == 'ii' or input == 'aa' or input == 'uu' :
                print('<',input,'> is not acceptable.', sep='')
            else :
                print('<',input,'> is acceptable.', sep='')
        else :
            print('<',input,'> is not acceptable.', sep='')
    else :
        for i in range(N-1) :
            if input[i:i+2] != 'ee' and input[i:i+2] != 'oo' and input[i] == input[i+1]  :
                print('<',input,'> is not acceptable.', sep='')
                passed = True
                break
        if not passed :        
            for i in range(N-2) :
                if input[i] in vowels and input[i+1] in vowels and input[i+2] in vowels :
                    print('<',input,'> is not acceptable.', sep='')
                    passed = True
                    break
                elif input[i] not in vowels and input[i+1] not in vowels and input[i+2] not in vowels :
                    print('<',input,'> is not acceptable.', sep='')
                    passed = True
                    break
        if not passed :
            for i in range(N) :
                if input[i] in vowels :
                    print('<',input,'> is acceptable.', sep='')
                    passed = True
                    break
        if not passed :
            print('<',input,'> is not acceptable.', sep='')