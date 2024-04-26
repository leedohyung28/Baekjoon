def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    
    ans = {
        6: 1, 
        5: 2, 
        4: 3, 
        3: 4, 
        2: 5, 
        1: 6, 
        0: 6}
    
    answer = 0
    zero = 0
    for l in lottos :
        if l == 0 :
            zero += 1
            continue
        
        for w in win_nums :
            if l == w :
                answer += 1
                break
    return [ans[zero+answer], ans[answer]]