import sys
import heapq

input = sys.stdin.readline
hq = []
result = []
N = int(input())

for i in range(N):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(hq))
    else:
        heapq.heappush(hq, num)

for num in result:
    print(num)