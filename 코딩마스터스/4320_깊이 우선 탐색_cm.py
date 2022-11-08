import sys

N, M = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(M):
    k,v = map(int, sys.stdin.readline().split())
    if k in graph:
        graph[k] = [v]
    else:
        graph[k].append(v)
    
def DFS(V, E, C)