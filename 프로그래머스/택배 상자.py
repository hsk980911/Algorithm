from collections import deque

def solution(order):
    main = [i for i in range(1,len(order)+1)]
    sub = []
    
    cnt = 0
    for i in order:
        if len(main) > 0 and main[0] <= i:
            sub.extend(main[:i-main[0]])
            main = main[i-main[0]+1:]
            cnt += 1
            continue
        elif sub:
            if sub[-1] == i:
                sub.pop()
                cnt += 1
                continue
            else:
                break
        else:
            break       
    return cnt