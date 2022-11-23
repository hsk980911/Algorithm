import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cand = []
    for _ in range(N):
        cand.append(tuple(map(int, sys.stdin.readline().split())))
    cand.sort(key = lambda x:x[0])
    
    cnt = 0
    low = N+1
    for i,j in cand:
       if low > j:
           low = j
           cnt += 1
    print(cnt)    