import sys

num = 1
for i in range(3):
    num *= int(sys.stdin.readline())

num = list(str(num))

cnt = {str(i):0 for i in range(10)}
for i in num:
    cnt[i] += 1
    
for i in cnt.values():
    print(i)