T = int(input())
for t in range(T):
    M, N = map(int, input().split())
    dp = [[0] * (N+1) for _ in range(M+1)]
    for i in range(1, N+1):
        dp[0][i] = 1
    for m in range(1, M+1):
        for n in range(1, N+1):
            if m < n:
                dp[m][n] = dp[m][m]
            else:
                dp[m][n] = dp[m][n-1] + dp[m-n][n]
    print(dp[M][N])
