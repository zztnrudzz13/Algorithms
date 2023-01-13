def solution(expression):
    answer = 0
    order = [('+', '-', '*'), ('-', '+', '*'), ('+', '*', '-'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]

    num = ''
    arr = []
    for i in expression:
        if i.isnumeric():
            num += i
        else:
            arr.append(num)
            arr.append(i)
            num = ''
    arr.append(num)

    def calculate(s, arr):
        result = []
        end = len(arr)
        i = 0
        while i < end:
            if arr[i] == s:
                front = result.pop()
                back = arr[i + 1]
                i += 1
                tmp = front + s + back
                result.append(str(eval(tmp)))
            else:
                result.append(arr[i])
            i += 1
        return result

    for a, b, c in order:
        tmp1 = calculate(a, arr)
        tmp2 = calculate(b, tmp1)
        tmp3 = calculate(c, tmp2)
        answer = answer if answer > abs(int(tmp3[0])) else abs(int(tmp3[0]))

    return answer