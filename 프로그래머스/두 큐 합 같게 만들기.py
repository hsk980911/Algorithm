from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if (sum(q1)+sum(q2)) % 2 == 1:
        return -1
    else:
        target = (sum(q1)+sum(q2)) // 2
    
    cnt = 0
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    while True:
        if target == sum1:
            return cnt
        if target < sum1:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        cnt += 1
        if cnt > len(queue1)*3:
            return -1
    return -1