import sys

N = int(sys.stdin.readline())
tmp =  [1, 3] + [0]*(N-2)

for i in range(2, len(tmp)):
    tmp[i] = tmp[i-1] + tmp[i-2]*2
print(tmp[-1])

# 못풀겠다...