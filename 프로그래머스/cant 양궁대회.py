def solution(n, info):
    answer = [0]*11
    expected_score = []
    
    for i in range(len(info)):
        if info[i] > 0:
            expected_score.append((10-i)*2/(info[i]+1))
        else:
            expected_score.append((10-i)/(info[i]+1))
    
    while n>0:
        if expected_score.count(0) == len(expected_score):
            answer[-1] += n
            n = 0
        
        tmp = expected_score.index(max(expected_score))
        if n < info[tmp]+1:
            expected_score[tmp] = 0
            continue
        else:
            n -= info[tmp]+1
            answer[tmp] = info[tmp]+1
            expected_score[tmp] = 0    
    a = 0
    l = 0
    for i in range(len(answer)):
        if answer[i] > 0 and info[i] > 0:
            if answer[i] > info[i]:
                l += 10-i
            else:
                a += 10-i
        elif answer[i] > 0 and info[i] == 0:
            l += 10-i
        elif info[i] > 0 and answer[i] == 0:
            a += 10-i
    if l > a:    
        return answer
    else:
        return [-1]