import sys
input = sys.stdin.readline
N = int(input())
digit = [0] * (N + 1)
current = [1] * 10

if N == 1:
    digit[1] = 10

if N >= 2:
    digit[1] = 10
    current = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for d in range(2, len(digit)):
        for i in range(1, len(current)):
            current[i] = current[i-1] + current[i]

        digit[d] = sum(current) % 10007

print(sum(digit) % 10007)