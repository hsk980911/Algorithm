import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    
    temp = [0]*(n+1)
    rooms = []
    for i in range(k+1):
        rooms.append(temp.copy())
    for i in range(n+1):
        rooms[0][i] = i
    for i in range(1, k+1):
        for j in range(1, n+1):
            print(rooms[i][j-1] + rooms[i][j-1])
            rooms[i][j] = rooms[i][j-1] + rooms[i][j-1]
    print(rooms)