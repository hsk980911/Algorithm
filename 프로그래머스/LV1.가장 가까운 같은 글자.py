def solution(s):
    info = {chr(i):-1 for i in range(ord('a'), ord('z')+1)}
    answer = []
    for i in range(len(s)):
        if info[s[i]] == -1:
            answer.append(-1)
        else:
            answer.append(i - info[s[i]])
        info[s[i]] = i
    return answer