def solution(n, t, m, timetable):
    answer = ''
    
    waits = []
    for i in timetable :
        h, mn = i.split(':')
        waits.append(int(h)*60+int(mn))
        
    waits.sort(reverse=True)
    
    bus = 540
    for k in range(n) :
        tmp_m = m
        dec = len(waits)
        for j in range(len(waits)-1, -1, -1) :
            if waits[j] <= bus :
                tmp_m -= 1
                dec = j
                if tmp_m == 0 :
                    if k == n-1 :
                        h = (waits[j]-1) // 60
                        mn = (waits[j]-1) % 60
                        answer = str(h).zfill(2)+':'+str(mn).zfill(2)
                        return answer
                    break
        if k == n-1 :
            h = bus // 60
            mn = bus % 60
            answer = str(h).zfill(2)+':'+str(mn).zfill(2)
            return answer

        waits = waits[:dec]
        bus += t
                    
            
    return answer