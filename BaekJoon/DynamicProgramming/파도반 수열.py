import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()[:-1]))

arr_max = max(arr)

L = [1, 1, 1, 2]

for i in range(4, arr_max+1):
        L.append(L[i-2] + L[i-3])

for num in arr:
    print(L[num-1])