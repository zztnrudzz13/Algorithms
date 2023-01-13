import sys
import heapq

input = sys.stdin.readline
N = int(input())
hq = []
result = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            result.append(0)
        else:
            tmp = heapq.heappop(hq)
            result.append(-tmp)
    else:
        heapq.heappush(hq, -num)

for num in result:
    print(num)

