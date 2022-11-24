import sys
from collections import deque

N = int(sys.stdin.readline())
cnt = 0
tmp = deque([N])

while True:
    if 1 in tmp: break
    cnt += 1
    for _ in range(len(tmp)):
        num = tmp.popleft()
        if num%3==0: tmp.append(int(num//3))
        if num%2==0: tmp.append(int(num//2))
        tmp.append(num-1)
print(cnt)
    
    