import sys
from collections import deque

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

arms ={}
for i in range(1, N+1):
    arms[i]:int(sys.stdin.readline())

dq = [1]

cnt = 0
while dq:
    cnt += 1
    for i in range(len(dq)):
        for k in arms:
            if arms[k] == dq[0]:
                dq.append(k)
        dq.popleft()
print(cnt)
            
    