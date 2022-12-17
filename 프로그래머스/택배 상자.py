from collections import deque

def solution(order):
    main = [i for i in range(1,len(order)+1)]
    sub = []
    
    cnt = 0
    for i in order:
        if sub:
            if sub[-1] == i:
                sub.pop()
                cnt += 1
            else:
                return cnt
        elif i in main:
            sub.extend(main[:main.index(i)])
            main = main[main.index(i)+1:]
            cnt += 1
        else:
            return cnt
    return cnt