import sys
input = sys.stdin.readline

N, M = input().split()
s1 = set()
s2 = set()

for i in range(int(N)):
    tmp = input()
    s1.add(tmp[0:-1])

for i in range(int(M)):
    tmp = input()
    s2.add(tmp[0:-1])

result = s1 & s2
print(len(result))
l = sorted(list(result))
for word in l:
    print(word)
