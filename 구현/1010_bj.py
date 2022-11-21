import sys
def factorial(start, end):
    f = 1
    for i in range(start, end+1):
        f *= i
    return f
    
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(factorial(N+1, M)/factorial(1, M-N)))