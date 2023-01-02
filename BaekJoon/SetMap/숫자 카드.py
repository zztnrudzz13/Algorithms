import sys
input = sys.stdin.readline

N = int(input())
L1 = list(map(int, input().split()))
dic = {}

for i in L1:
    dic[i] = 1

M = int(input())
L2 = list(map(int, input().split()))
result = []

for i in L2:
    try:
        result.append(dic[i])
    except:
        result.append(0)

for num in result:
    print(num, end=' ')