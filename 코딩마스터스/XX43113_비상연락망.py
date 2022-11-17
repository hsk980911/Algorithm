import sys
from collections import deque

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

arms ={}
for i in range(len(M)):
    if M[i] in arms:
        arms[M[i]].append(i+1)
    else:
        arms[M[i]] = [i+1]
arms = sorted(arms.items(), key=lambda x:x[0])

arms = dict(arms)
received = arms[1].copy()
tmp = arms[1].copy()
del arms[1]

cnt = 1

while True:
    if len(received) == N:
        print(cnt)
        break
       
    cnt += 1
    tmp2 = []
    for i in tmp:
        if i in arms:
            received += arms[i]
            tmp2 += arms[i]
            del arms[i]
    tmp = tmp2.copy()
        