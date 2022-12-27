from collections import deque

def solution(numbers, target):
    answer = 0
    dq = deque([[numbers[0], 0], [-numbers[0],0]])
    while dq:
        tmp, idx = dq.popleft()
        
        if idx == len(numbers)-2:
            if tmp + numbers[idx+1] == target:
                answer += 1
            if tmp - numbers[idx+1] == target:
                answer += 1
        else:
            dq.append([tmp + numbers[idx+1], idx+1])
            dq.append([tmp - numbers[idx+1], idx+1])
    return answer