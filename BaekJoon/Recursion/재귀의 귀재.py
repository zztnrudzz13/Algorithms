import sys
input = sys.stdin.readline

N = int(input())
L = []

for i in range(N):
    tmp = input()
    L.append([tmp[0:-1], 0])

def recursion(s, l, r, num):
    if l >= r:
        return [1, num]
    elif s[l] != s[r]:
        return [0, num]
    else:
        num += 1
        return recursion(s, l+1, r-1, num)

def isPalindrome(s, num):
    num += 1
    return recursion(s, 0, len(s)-1, num)

for arr in L:
    s, n = arr[0], arr[1]
    b, num = isPalindrome(s, n)
    print(b, num)