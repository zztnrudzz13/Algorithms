import sys

input = sys.stdin.readline
n = int(input())
result = 0

arr = list(map(int, input().split()))
arr.sort()

x = int(input())

s = 0
e = len(arr) - 1

while s < e:
    tmp = arr[s] + arr[e]
    if tmp > x:
        e -= 1
    elif tmp == x:
        result += 1
        s += 1
    elif tmp < x:
        s += 1

print(result)

