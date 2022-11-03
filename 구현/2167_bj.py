import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    # arr.append(list(map(int, sys.stdin.readline().split())))
    arr.extend(list(map(int, sys.stdin.readline().split())))
    
k = int(sys.stdin.readline())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    if i == x and j == y:
        print(arr[(i-1)*M + (j-1)])
    elif i == x:
        print(sum(arr[(i-1)*M + (j-1) : (i-1)*M + (j-1) + (y-j+1)]))
    elif j == y:
        s = 0
        for rows in range(i, x+1):
            s += arr[(rows-1)*M +(j-1)]
        print(s)    
    else:
        print(sum(arr[(i-1)*M + (j-1):(x-1)*M + (y-1)+1]))
    # tmp = []
    # for row in range(i-1, x):
    #     tmp.append(arr[row][j-1:y])
    #     tmp2 = sum(tmp, [])
    #     print(sum(tmp2))
