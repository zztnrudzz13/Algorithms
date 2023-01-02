import sys
input = sys.stdin.readline

N = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))

curr = 0
step = 1
result = 0

while curr < N and step < N:
    if C[curr] <= C[step]:
        result += C[curr] * R[step-1]
        step += 1
    else:
        result += C[curr] * R[step-1]
        curr = step
        step = curr + 1

print(result)