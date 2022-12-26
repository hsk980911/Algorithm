def solution(d, budget):
    d.sort()
    
    cnt = 0
    for cost in d:
        if budget - cost < 0:
            return cnt
        else:
            budget -= cost
            cnt += 1
    return cnt