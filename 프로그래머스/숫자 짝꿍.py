def solution(X, Y):
    answer = []
    X = list(X)
    Y = list(Y)
    for i in X:
        if i in Y:
            answer.append(i)
            Y.remove(i)
    answer.sort(reverse=True)
    answer = ''.join(answer)
    
    if len(answer) == 0:
        return '-1'
    else:
        return str(int(answer))