import math

def solution(fees, records):
    answer = []
    
    in_time = {}
    total = {}
    cars = {}
    for i in records :
        a, b, c = i.split()
        if c == 'IN' :
            in_time[b] = a
            cars[b] = False
        
        else :
            ha, ma = map(int, a.split(':'))
            hb, mb = map(int, in_time[b].split(':'))
            if ma >= mb :
                if b not in total :
                    total[b] = (ha-hb) * 60 + ma-mb
                else :
                    total[b] += (ha-hb) * 60 + ma-mb
            
            else :
                if b not in total :
                    total[b] = (ha-hb-1) * 60 + ma+60-mb
                else :
                    total[b] += (ha-hb-1) * 60 + ma+60-mb
            cars[b] = True

    for i in cars :
        if not cars[i] :
            hb, mb = map(int, in_time[i].split(':'))
            if i not in total :
                total[i] = (23-hb) * 60 + 59-mb
            else :
                total[i] += (23-hb) * 60 + 59-mb
    
    K = sorted(cars.keys())
    for i in K :
        toll = fees[1]
        if total[i] > fees[0] :
            toll += math.ceil((total[i] - fees[0]) / fees[2]) * fees[3]
        
        answer.append(toll)
    
    return answer