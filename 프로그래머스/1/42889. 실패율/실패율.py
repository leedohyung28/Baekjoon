def solution(N, stages):
    answer = []
    
    end = [0] * N
    total = [len(stages)] * N
    for i in stages :
        if i <= N :
            end[i-1] += 1
    
    s = 0
    percent = []
    for i in range(N-1) :
        s += end[i]
        total[i+1] -= s
        if total[i] == 0 :
            percent.append([0, i+1])
        else :
            percent.append([end[i]/total[i], i+1])
    
    if total[-1] == 0 :
        percent.append([0, N])
    else :
        percent.append([end[-1]/total[-1], N])

    percent.sort(key=lambda x:x[0], reverse=True)
    for i in percent :
        answer.append(i[1])
    
    return answer