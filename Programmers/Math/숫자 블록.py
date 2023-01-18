def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        sqrt = int(i ** 0.5)
        count = 2
        switch = True
        if i == 1:
            answer.append(0)
            switch = False
        while count <= sqrt and switch:
            if i % count == 0 and i / count <= 10000000:
                answer.append(int(i / count))
                switch = False
            count += 1
        if switch == True:
            answer.append(1)

    return answer