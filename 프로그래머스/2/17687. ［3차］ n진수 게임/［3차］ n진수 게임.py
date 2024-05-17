def tenton(num, n) :
    
    change = {
        10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F'
    }
    
    output = ''
    while num > 0 :
        if num % n >= 10 :
            output = change[num%n] + output
        else :
            output = str(num%n) + output
        num //= n
    
    return output

def solution(n, t, m, p):
    answer = ''
    
    num = 0
    str_num = '0'
    turn = 1
    while True :
        
        for i in str_num :
            if turn == p :
                answer += i
                t -= 1
                
                if t == 0 :
                    return answer
                
            if turn == m :
                turn = 0
            turn += 1
        
        num += 1
        str_num = tenton(num, n)