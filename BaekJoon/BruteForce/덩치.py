import sys
input = sys.stdin.readline

N = int(input())
L = []
result = [0 for i in range(N)]

for i in range(N):
   tmp = list(map(int, input().split()))
   L.append(tmp)

for i in range(len(L)):
    weight = L[i][0]
    height = L[i][1]
    for j in range(i+1, len(L)):
        c_weight = L[j][0]
        c_height = L[j][1]
        if weight > c_weight and height > c_height:
            result[j] += 1
        elif weight < c_weight and height < c_height:
            result[i] += 1

for num in result:
    print(num+1, end=' ')




