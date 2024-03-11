from collections import deque

def backtrack(answer, depart, N, ticks, vis) :
    if len(answer) == N + 1 :
        return True
    arrivals = []
    for i in range(N) :
        if vis[i] is False and depart == ticks[i][0] :
            arrivals.append([ticks[i][1], i])
    arrivals.sort(reverse=True)
    while arrivals :
        v = arrivals.pop()
        vis[v[1]] = True
        answer.append(v[0])
        true = backtrack(answer, v[0], N, ticks, vis)
        if true :
            return answer
        answer.pop()
        vis[v[1]] = False
    

def solution(tickets):
    answer = ['ICN']
    N = len(tickets)
    visited = [False] * (N+1)
    answer = backtrack(answer, 'ICN', N, tickets, visited)
    return answer