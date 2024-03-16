def solution(friends, gifts):
    answer = 0
    N = len(friends)
    gift_points = [0] * N
    give_n_take = [[0] * N for _ in range(N)]
    
    for m in gifts :
        give, take = m.split()
        give_num, take_num = -1, -1
        for i in range(N) :
            if friends[i] == give :
                gift_points[i] += 1
                give_num = i
            elif friends[i] == take :
                gift_points[i] -= 1
                take_num = i
            if give_num != -1 and take_num != -1 :
                give_n_take[give_num][take_num] += 1
                break
    
    get_presents = [0] * N
    for a in range(N-1) :
        for b in range(a+1, N) :
            if give_n_take[a][b] == give_n_take[b][a] :
                if gift_points[a] > gift_points[b] :
                    get_presents[a] += 1
                elif gift_points[b] > gift_points[a] :
                    get_presents[b] += 1
            elif give_n_take[a][b] > give_n_take[b][a] :
                get_presents[a] += 1
            else :
                get_presents[b] += 1
                        
    answer = max(get_presents)
    return answer