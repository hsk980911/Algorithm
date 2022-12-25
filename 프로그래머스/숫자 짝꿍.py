def solution(X, Y):
    answer = []
    for i in set(list(X))&set(list(Y)):
        answer += [i]*min(X.count(i), Y.count(i))
    answer.sort(reverse=True)
    answer = ''.join(answer)
    
    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer