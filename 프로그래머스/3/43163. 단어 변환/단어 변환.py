def check_valid(a, b, l) :
    check_once = False
    for i in range(l) :
        if a[i] != b[i] :
            if check_once :
                return False
            else :
                check_once = True
    return True
        
def solution(begin, target, words):
    answer = 0
    N = len(words)
    l = len(begin)
    stack = []
    visited = [51] * N
    
    for i in range(N) :
        if check_valid(begin, words[i], l) :
            visited[i] = 1
            stack.append(i)
    
    while stack :
        v = stack.pop()
        
        if words[v] == target :
            return visited[v]
        
        for i in range(N) :
            if visited[i] == 51 and check_valid(words[v], words[i], l) :
                stack.append(i)
                visited[i] = visited[v] + 1
    
    return answer