# BFS

from collections import deque
import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
d = [(-1,0), (1,0), (0,1), (0,-1)]
q = deque()

cnt = 0
cnt_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            cnt_house = 1
            q.append((i, j))
            graph[i][j] = 0
            while q:
                temp = q.popleft()
                x, y = temp[0], temp[1] 
                for k in d:
                    dx = x + k[0]
                    dy = y + k[1]
                    
                    if 0<=dx<N and 0<=dy<N:
                        if graph[dx][dy] == 1:
                            cnt_house += 1
                            q.append((dx, dy))
                            graph[dx][dy] = 0
            cnt_list.append(cnt_house)
print(cnt)
cnt_list.sort()
for i in cnt_list:
    print(i)
        