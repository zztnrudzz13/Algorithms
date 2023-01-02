import sys
input = sys.stdin.readline
L = []
switch = True

while switch:
    tmp = input()[:-1]
    if tmp == '.':
        switch = False
    else:
        L.append(tmp)

def check(s):
    S = []
    dic = {
        ')': '(',
        ']': '['
    }
    v = dic.values()
    k = dic.keys()
    for p in s:
        if p in v:
            S.append(p)
        if p in k:
            if len(S) != 0 and S[-1] == dic[p]:
                S.pop()
            else:
                return False
    return True if len(S) == 0 else False

for string in L:
    print('yes') if check(string) else print('no')