import sys
input = sys.stdin.readline

N = int(input())
stairs = []
result = [[0, 0] for i in range(N)]

for i in range(N):
    stairs.append(int(input()[:-1]))

result[0] = [0, stairs[0]]

if N > 1:
    result[1] = [stairs[0] + stairs[1], stairs[1]]

for i in range(2, len(stairs)):
    result[i][0] = result[i-1][1] + stairs[i]
    result[i][1] = max(result[i-2]) + stairs[i]

arr = result[-1]

print(max(arr))
