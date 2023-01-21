def solution(cap, n, deliveries, pickups):
    answer = 0
    c = cap
    d_point = []
    for i in range(len(deliveries) - 1, -1, -1):
        while deliveries[i] != 0:
            if c == cap:
                d_point.append(i)
            if c > 0 and deliveries[i] > 0:
                if c > deliveries[i]:
                    c -= deliveries[i]
                    deliveries[i] = 0
                elif c == deliveries[i]:
                    deliveries[i] = 0
                    c = cap
                else:
                    deliveries[i] -= c
                    c = cap
    c = cap
    p_point = []
    for i in range(len(pickups) - 1, -1, -1):
        while pickups[i] != 0:
            if c == cap:
                p_point.append(i)
            if c > 0 and pickups[i] > 0:
                if c > pickups[i]:
                    c -= pickups[i]
                    pickups[i] = 0
                elif c == pickups[i]:
                    pickups[i] = 0
                    c = cap
                else:
                    pickups[i] -= c
                    c = cap

    e = max(len(d_point), len(p_point))

    for i in range(e):
        d_m = 0
        p_m = 0
        if len(d_point) > i:
            d_m = d_point[i]
        if len(p_point) > i:
            p_m = p_point[i]

        answer += (max(d_m, p_m) + 1) * 2

    return answer