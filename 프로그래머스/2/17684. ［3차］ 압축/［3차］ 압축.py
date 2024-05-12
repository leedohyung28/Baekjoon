def solution(msg):
    alpha = {
        'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
        'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23,
        'X': 24, 'Y':25, 'Z':26
    }
    
    answer = []
    idx = 27
    
    i = 0
    while i < len(msg) :
        if i == len(msg)-1 :
            answer.append(alpha[msg[i]])
            break
        
        l = 1
        while i+l <= len(msg) :
            if i+l == len(msg) and msg[i:i+l] in alpha :
                answer.append(alpha[msg[i:i+l]])
            
            if msg[i:i+l] not in alpha :
                alpha[msg[i:i+l]] = idx
                idx += 1
                answer.append(alpha[msg[i:i+l-1]])
                break
            l += 1
        i += l-1
    return answer