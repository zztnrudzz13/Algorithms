import sys
input = sys.stdin.readline

N, M = input().split()
s = set()
l = []

for i in range(int(N)):
    s.add(input()[0:-1])

for i in range(int(M)):
    l.append(input()[0:-1])

result = 0

for word in l:
    if word in s:
        result += 1
print(result)
