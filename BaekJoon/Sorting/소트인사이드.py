N = int(input())

L = list(str(N))
L.sort(reverse=True)
N = int(''.join(L))

print(N)
