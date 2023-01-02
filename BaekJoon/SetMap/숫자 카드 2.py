import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
s = {}

for i in range(N):
    try:
        s[l[i]] += 1
    except:
        s[l[i]] = 1

M = int(input())
a = list(map(int, input().split()))
result = []
for i in range(M):
    try:
        result.append(s[a[i]])
    except:
        result.append(0)

for num in result:
    print(num, end=" ")