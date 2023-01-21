import sys
from collections import deque
T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for i in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    
    dxdy = [(0,1), (0,-1), (1,0), (-1,0)]
    cnt = 0
    q = deque()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                q.append((i,j))
                arr[i][j] == 0
                cnt += 1
                while q:
                    temp = q.popleft()
                    for d in dxdy:
                        x = d[1]+temp[1]
                        y = d[0]+temp[0]
                        if 0 <= x < len(arr[0]) and 0 <= y < len(arr) and arr[y][x] == 1:
                            arr[y][x] = 0
                            q.append((y,x))
    print(cnt)
                            
    