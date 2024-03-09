from collections import deque

def solution(n, computers):
    answer = 0
    
    connected = [False] * n
    
    for k in range(n) :
        if connected[k] is False :
            deq = deque([k])
            answer += 1

            while len(deq) != 0 :
                v = deq.popleft()
                connected[v] = True
                for i in range(n) :
                    if connected[i] is False and computers[v][i] == 1:
                        deq.append(i)

    return answer