import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

d = [(-1,0), (1,0), (0,1), (0,-1)]
q = deque()
q.append((0,0))

def bfs():
    while q:
        x, y = q.popleft()
        for k in d:
            dx = x + k[0]
            dy = y + k[1]
            if 0 <= dx <N and 0 <= dy < M:
                if graph[dx][dy] == 1:
                    graph[dx][dy] = graph[x][y] + 1
                    q.append((dx, dy))
graph[0][0] = 1
bfs()
print(graph[N-1][M-1])