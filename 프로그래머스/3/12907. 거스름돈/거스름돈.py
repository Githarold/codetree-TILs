def solution(n, money):
    MAX_NUM = 1000000007
    dp = [0] * (n+1)
    dp[0] = 1
    for m in money:
        for i in range(m, n+1):
            dp[i] += dp[i-m]
            dp[i] %= MAX_NUM
    return dp[n]
