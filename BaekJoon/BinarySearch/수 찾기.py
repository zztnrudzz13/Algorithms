import sys
input = sys.stdin.readline

N = int(input())
base = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

base.sort()

num = -1

def bs(left, right):
    mid = int((left + right) / 2)
    if right - left <= 1:
        if base[left] == num or base[right] == num:
            print(1)
        else:
            print(0)
    elif num == base[mid]:
        print(1)
    elif base[mid] > num:
        bs(left, mid-1)
    elif base[mid] < num:
        bs(mid+1, right)


for i in compare:
    num = i
    bs(0, len(base)-1)