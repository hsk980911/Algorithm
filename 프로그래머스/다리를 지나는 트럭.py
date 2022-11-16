from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    tw = deque(truck_weights)
    
    w = tw.popleft()
    q.append([w, 0])
    total = w
    
    cnt = 0
    while tw:
        cnt += 1
        for i in q:
            i[1] += 1
            
        if q[0][1] >= bridge_length:
            total -= q.popleft()[0]
        
        if total + tw[0] > weight:
            continue
        tmp = tw.popleft()
        q.append([tmp, 0])
        total += tmp
        
    print(q)
    print(tw)
        
    return cnt + bridge_length + 1