import sys

# def Fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return Fib(n-1) + Fib(n-2)
    
N = int(sys.stdin.readline())

fib = [0, 1] + [0]*(N-1)
for i in range(2, N+1):
    fib[i] = fib[i-1] + fib[i-2]
print(fib[-1])