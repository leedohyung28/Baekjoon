def solution(id_list, report, k):
    answer = []
    id_dict = {}
    ban = {}
    
    for v in id_list :
        ban[v] = 0
    
    for i in report :
        a, b = i.split()
        if a not in id_dict :
            id_dict[a] = set([b])
            ban[b] += 1
        elif b not in id_dict[a] :
            id_dict[a].add(b)
            ban[b] += 1
        
    for m in id_list :
        if m in id_dict :
            ans = 0
            for n in list(id_dict[m]) :
                if ban[n] >= k :
                    ans += 1
            answer.append(ans)
        else :
            answer.append(0)
            
    return answer