import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    race_list = list(map(int, sys.stdin.readline().split()))
    
    data_dict = dict()
    for i in race_list :
        if i in data_dict :
            data_dict[i] += 1
        else :
            data_dict[i] = 1
    
    race = set()    
    for k in range(1, 201) :
        if k not in data_dict :
            break
        if data_dict[k] >= 6 :
            race.add(k)
    
    point_list = [0] * 201
    top_four = [4] * 201
    fifth_racers = []
    point = 0
    for m in race_list :
        if m not in race :
            continue
        else :
            point += 1
            if top_four[m] > 0 :
                top_four[m] -= 1
                point_list[m] += point
            elif top_four[m] == 0 :
                fifth_racers.append(m)
                top_four[m] -= 1
    min = float('inf')
    for n in race :
        if point_list[n] < min :
            min = point_list[n]
            results = []
            results.append(n)
        elif point_list[n] == min :
            results.append(n)
            
    if len(results) == 1 :
        print(results[0])
    else :
        for j in fifth_racers :
            if j in results :
                print(j)
                break