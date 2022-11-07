import sys

N = int(sys.stdin.readline())
stocks = [0]*(N+1)
for _ in range(N):
    shoe = int(sys.stdin.readline())
    stocks[shoe] += 1
print(stocks)
stocks.reverse()
print(stocks)
print(N - stocks.index(max(stocks)))