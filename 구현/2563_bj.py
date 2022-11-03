# 못풀음
import sys

N = int(sys.stdin.readline())
area = 0
dots = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    area += 100
    
    for d in dots:
        i = d[0]; j = d[1]
        if abs(x-i) < 10 and abs(y-j) < 10:
            area -= (10-abs(x-i))*(10-abs(y-j))
    dots.append((x, y))

print(area)