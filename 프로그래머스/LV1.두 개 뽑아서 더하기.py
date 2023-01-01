from itertools import combinations

def solution(numbers):
    answer = []
    comb = combinations(numbers,2)
    
    for i in comb:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    
    return answer