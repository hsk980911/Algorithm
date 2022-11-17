def length(s, n):
    l = ''
    cnt = 1
    for i in range(0,len(s),n):
        if s[i:i+n] == s[i+n:i+2*n]:
            cnt += 1
        else:
            if cnt == 1:
                l += s[i:i+n]
            else:
                l += str(cnt)+s[i:i+n]
                cnt = 1
    return len(l)

def solution(s):
    short = len(s)
    for n in range(1, len(s)+1):
        tmp = length(s,n)
        if short > tmp:
            short = tmp
    return short