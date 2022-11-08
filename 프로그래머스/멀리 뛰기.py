
def solution(n):
    dp = [1,2]
    
    for i in range(2, n):
        dp.append(dp[-1]+dp[-2])
    if n == 1:
        return dp[0]
    else:
        return dp[-1] % 1234567