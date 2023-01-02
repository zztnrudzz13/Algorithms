import sys
input = sys.stdin.readline

N, M = input().split()
d = {}
c_d = {}
a = []

for i in range(int(N)):
    tmp = input()
    d[i+1] = tmp

c_d = {v:k for k,v in d.items()}

for i in range(int(M)):
    a.append(input())

result = []
for word in a:
    try:
        num = int(word)
        result.append(d[num][0:-1])
    except:
        result.append(str(c_d[word]))

for word in result:
    print(word)
