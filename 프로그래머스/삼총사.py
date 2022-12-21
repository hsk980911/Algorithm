from itertools import combinations

def solution(number):
    comb = list(combinations(number, 3))
    cnt = 0
    for c in comb:
        if sum(c) == 0:
            cnt += 1
    return cnt