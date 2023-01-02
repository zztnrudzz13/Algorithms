import sys
input = sys.stdin.readline

l = input()[:-1].split('-')
result = 0

def plus(s):
    r = 0
    arr = list(map(int, s.split('+')))
    for num in arr:
        r += num
    return r

if l[0] == '':
    result -= plus(l[1])
    l = l[2:]
else:
    result += plus(l[0])
    l = l[1:]

for string in l:
    result -= plus(string)

print(result)
