import sys

N = int(sys.stdin.readline())

loc = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
d_total = []

for i in range(len(loc)):
    tmp = loc.copy()
    tmp.pop(i)
    d = 0
    for j in tmp:
        d += abs(loc[i][0] - j[0]) * j[1]
    d_total.append(d)
print(d_total.index(min(d_total))+1)