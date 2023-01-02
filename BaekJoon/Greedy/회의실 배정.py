import sys
input = sys.stdin.readline

N = int(input())
L = []


for i in range(N):
    tmp = list(map(int, input()[:-1].split()))
    L.append(tmp)

L.sort(key=lambda x: (x[1], x[0]))

result = 1
end = L[0][1]
i = 1

while i < len(L):
    if L[i][0] >= end:
        end = L[i][1]
        result += 1
    i += 1


print(result)



