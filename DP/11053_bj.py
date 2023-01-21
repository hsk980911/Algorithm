import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * len(arr)

for i in range(len(arr)):
    for j in range(i):
        if dp[i] <= dp[j] and arr[i] > arr[j]:
            dp[i] = dp[j]+1
print(max(dp))