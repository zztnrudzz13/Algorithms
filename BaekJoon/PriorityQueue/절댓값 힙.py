import sys
import heapq

input = sys.stdin.readline
mhq = []
phq = []
result = []

N = int(input())

for i in range(N):
    num = int(input())
    if num == 0:
        if len(mhq) > 0 and len(phq) > 0:
            m = mhq[0]
            p = phq[0]
            if m <= p:
                tmp = heapq.heappop(mhq)
                result.append(-tmp)
            elif m > p:
                result.append(heapq.heappop(phq))
        elif len(mhq) == 0 and len(phq) > 0:
            result.append(heapq.heappop(phq))
        elif len(phq) == 0 and len(mhq) > 0:
            tmp = heapq.heappop(mhq)
            result.append(-tmp)
        else:
            result.append(0)
    else:
        if num > 0:
            heapq.heappush(phq, num)
        elif num < 0:
            heapq.heappush(mhq, -num)

for num in result:
    print(num)