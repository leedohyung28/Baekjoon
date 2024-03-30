def prime(n) :
    if n == 1 :
        return False
    for i in range(2, int(n**(1/2))+1) :
        if n % i == 0 :
            return False
    return True

def solution(n, k):
    answer = 0
    
    a = ''
    while n > 0 :
        a = str(n % k) + a
        n //= k
        
    c = ''
    for i in a :
        if i == '0' :
            if len(c) > 0 and prime(int(c)) :
                answer += 1
            c = ''
        else :
            c += i
    if len(c) > 0 and prime(int(c)) :
        answer += 1
        
    return answer