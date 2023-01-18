import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    arr[W] = arr[W] if arr[W] > V else V

for i in range(len(arr)):
    half = int(i / 2) + 1
    for j in range(half, i):
        l = i - j
        arr[i] = arr[i] if arr[i] > arr[j] + arr[l] else arr[j] + arr[l]

print(arr[-1])
