def solution(book_time):
    
    all_times = []
    for s, e in book_time :
        sh, sm = s.split(':')
        all_times.append([int(sh)*60+int(sm), 'in'])
        eh, em = e.split(':')
        all_times.append([int(eh)*60+int(em)+9.5, 'out'])
    
    all_times.sort()
    answer = 0
    
    rooms = 0
    for _, k in all_times :
        if k == 'in' :
            rooms += 1
        else :
            answer = max(answer, rooms)
            rooms -= 1
    
    return answer