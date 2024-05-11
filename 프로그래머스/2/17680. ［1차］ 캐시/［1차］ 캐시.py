from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    d = deque()
    dSize = 0
    
    if cacheSize == 0 :
        return len(cities)*5
    
    for city in cities :
        city = city.lower()
        
        if city in d :
            answer -= 4
            d.remove(city)
        
        elif dSize < cacheSize :
            dSize += 1
        
        else :
            d.popleft()
        
        d.append(city)
        answer += 5
    
    return answer