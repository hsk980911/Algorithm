def solution(n, lost, reserve):
    all = [1 for i in range(n+2)]
    
    for i in lost:
        all[i] -= 1
    for i in reserve:
        all[i] += 1
    
    for i in range(1,len(all)-1):
        if all[i] > 1:
            if all[i-1] == 0:
                all[i-1] += 1
                all[i] -= 1
            elif all[i+1] == 0:
                all[i+1] += 1
                all[i] -= 1
                
    return n-all.count(0)