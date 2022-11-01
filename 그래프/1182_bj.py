# DFS

import sys

N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

def Recur(sum, idx):
    global cnt
    if idx >= N:
        return
    sum += num_list[idx]
    if sum == S:
         cnt+=1
    return Recur(sum, idx+1), Recur(sum-num_list[idx], idx+1)

cnt = 0
Recur(0,0)
print(cnt)