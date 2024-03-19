def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0] * n for _ in range(n)]
    
    for chain_len in range(2, n+1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] \
                + matrix_sizes[i][0]*matrix_sizes[k][1]*matrix_sizes[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    return dp[0][n-1]