def solution(cards):
    o = [False for i in range(len(cards))]
    g = []
    cnt = [0]

    def check(arr, i, c):
        if o[i - 1]:
            return
        else:
            num = cards[i - 1]
            o[i - 1] = True
            arr.append(num)
            c[0] += 1
            check(arr, num, c)

    i = 0
    while cnt[0] != len(cards):
        tmp = []
        check(tmp, i, cnt)
        if len(tmp) > 0:
            g.append(tmp)
        i += 1

    if len(g) == 1:
        return 0

    result = [len(arr) for arr in g]
    result.sort()

    return result[-1] * result[-2]