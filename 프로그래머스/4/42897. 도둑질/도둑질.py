def solution(money):
    N = len(money)
    dp = [0] * N
    dp_visited = [0] * N
    
    dp_visited[0] = money[0]
    dp[1] = money[1]
    dp_visited[1] = max(money[0], money[1])
    
    for i in range(2, N-1) :
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
        dp_visited[i] = max(dp_visited[i-2]+money[i], dp_visited[i-1])
        
    dp[-1] = max(dp[-3]+money[-1], dp[-2])
    dp_visited[-1] = max(dp_visited[-3], dp_visited[-2], dp_visited[-3]-money[0]+money[-1])
    
    return max(dp[-1], dp_visited[-1])