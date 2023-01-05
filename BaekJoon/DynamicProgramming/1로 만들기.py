import sys
import math
input = sys.stdin.readline

N = int(input())
result = [0 for i in range(N+1)]
result[0] = 0
result[1] = 0

for i in range(2, N+1):
    minus = result[i - 1]
    two = math.inf if i % 2 != 0 else result[int(i / 2)]
    three = math.inf if i % 3 != 0 else result[int(i / 3)]
    result[i] = min([minus, two, three]) + 1

print(result[-1])