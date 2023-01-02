import re
import sys
input = sys.stdin.readline
regex = re.compile("666")

N = int(input())
num = 0

while N > 0:
    if regex.search(str(num)) is not None:
        N -= 1
    if N == 0:
        break
    num += 1

print(num)


