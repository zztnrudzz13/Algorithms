import sys
input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

if len(arr) == 1:
    print(arr[0][0])
elif len(arr) == 2:
    print(max(arr[0][0] + arr[1][0], arr[0][0] + arr[1][1]))
elif len(arr) >= 3:
    arr[1][0] = arr[1][0] + arr[0][0]
    arr[1][1] = arr[1][1] + arr[0][0]
    for i in range(2, N):
        arr[i][0] = arr[i][0] + arr[i-1][0]
        arr[i][-1] = arr[i][-1] + arr[i-1][-1]
        for j in range(1, i):
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]
    print(max(arr[-1]))