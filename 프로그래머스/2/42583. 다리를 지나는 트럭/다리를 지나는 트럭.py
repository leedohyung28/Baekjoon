from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    timeDeque = deque([])
    bridge = deque([])
    while truck_weights :
        v = truck_weights.pop()
        time += 1
        
        if len(timeDeque) > 0 and time - timeDeque[0] == bridge_length :
            timeDeque.popleft()
            weight += bridge.popleft()
        
        while weight - v < 0 :
            time = bridge_length + timeDeque.popleft()
            weight += bridge.popleft()
        
        weight -= v
        bridge.append(v)
        timeDeque.append(time)
            
    time = bridge_length + timeDeque[-1]
    
    return time