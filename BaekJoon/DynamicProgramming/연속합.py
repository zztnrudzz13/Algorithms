import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_num = arr[0]

for i in range(1, len(arr)):
    if arr[i-1] > 0 and arr[i] + arr[i-1] > 0:
        arr[i] += arr[i-1]

    if max_num < arr[i]:
        max_num = arr[i]

print(max_num)