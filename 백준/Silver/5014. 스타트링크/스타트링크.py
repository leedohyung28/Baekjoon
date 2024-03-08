import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())

result = 0                  # 결과
visited = [False] * F       # 방문

while S != G :  # 같을 때 까지 반복
    
    # 방문 체크
    visited[S-1] = True
    
    # 더 아래에 건물이 있다면
    if S > G :
        if S - D < 1 :  # 아래로 내려갔을 때 0층 이하면
            S += U      # 위로 간다
            result += 1
            
            # 최대층을 넘거나 방문했으면 use the stairs
            if S > F or visited[S-1] :
                print('use the stairs')
                exit()
        else :
            S -= D          # 아래로 간다
            result += 1
        
        # 0층 이하로 가거나 방문했다면 use the stairs
        if S < 1 or visited[S-1] :
            print('use the stairs')
            exit()
            
    # 건물이 위에 있다면
    else :
        if S + U > F :  # 올라갔을 때 최대층 넘으면
            S -= D      # 아래로 간다
            result += 1
            
            # 0층 이하거나 방문했다면 use the stairs
            if S < 1 or visited[S-1] :
                print('use the stairs')
                exit()
                
        else :
            S += U      # 위로 간다
            result += 1
        
        # 최대층 넘거나 방문했다면 use the stairs
        if S > F or visited[S-1] :
            print('use the stairs')
            exit()

print(result)