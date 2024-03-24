def solution(genres, plays):
    answer = []
    
    s = {}
    no = {}
    nu = {}
    
    for i in range(len(genres)) :
        if genres[i] not in s :
            s[genres[i]] = plays[i]
            no[genres[i]] = [i]
            nu[genres[i]] = [plays[i]]
        else :
            s[genres[i]] += plays[i]
            if len(no[genres[i]]) == 1 :
                if plays[i] > nu[genres[i]][0] :
                    nu[genres[i]].insert(0, plays[i])
                    no[genres[i]].insert(0, i)
                else :
                    nu[genres[i]].append(plays[i])
                    no[genres[i]].append(i)
            else :
                if plays[i] > nu[genres[i]][0] :
                    nu[genres[i]].insert(0, plays[i])
                    no[genres[i]].insert(0, i)
                    nu[genres[i]].pop()
                    no[genres[i]].pop()
                elif plays[i] > nu[genres[i]][1] :
                    nu[genres[i]].insert(1, plays[i])
                    no[genres[i]].insert(1, i)
                    nu[genres[i]].pop()
                    no[genres[i]].pop()          
    
    mp = sorted(s.items(), key=lambda x: x[1], reverse=True)
    for i in mp :
        answer.extend(no[i[0]])
    
    
    return answer