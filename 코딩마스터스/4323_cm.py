import sys

N, M = map(int, sys.stdin.readline().split())
P = list(map(int, sys.stdin.readline().split()))
P.sort(reverse=True)
cnt = 0
for i in P:
    if N == 0: break
    elif N-i < 0:
        continue
    else:
        N -= i
        cnt += 1
print(cnt)
