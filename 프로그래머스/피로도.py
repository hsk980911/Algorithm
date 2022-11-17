from itertools import permutations

def cal(k, dungeons, order):
    cnt = 0
    tired = k
    for i in order:
        if dungeons[i][0] > tired:
            break
        else:
            cnt += 1
            tired -= dungeons[i][1]
    return cnt

def solution(k, dungeons):
    answer = -1
    p = permutations([i for i in range(0, len(dungeons))], len(dungeons))
    cases = []
    for order in p:
        cases.append(cal(k, dungeons, order))
    return max(cases)