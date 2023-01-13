import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

if len(arr) == 1:
    print(arr[0])
elif len(arr) == 2:
    print(arr[0] + arr[1])
elif len(arr) >= 3:
    dp = [[0, 0, 0, 0, 0, 0] for i in range(N)]
    dp[2] = [arr[0]+arr[2], arr[0], arr[0]+arr[1], arr[1]+arr[2], arr[2], arr[1]]
    for i in range(3, len(dp)):
        dp[i][0] = max(dp[i-1][2] + arr[i], dp[i-1][5] + arr[i])
        dp[i][1] = max(dp[i-1][2], dp[i-1][5])
        dp[i][2] = dp[i-1][3]
        dp[i][3] = max(dp[i-1][0] + arr[i], dp[i-1][4] + arr[i])
        dp[i][4] = dp[i-1][1] + arr[i]
        dp[i][5] = max(dp[i-1][0], dp[i-1][4])

    print(max(dp[-1]))


