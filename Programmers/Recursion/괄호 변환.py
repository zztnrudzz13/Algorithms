from collections import Counter


def solution(p):
    answer = ''

    def checkRightBracket(s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return True

    def checkBalancedBracket(s):
        c = Counter(s)
        return c['('] == c[')']

    def reversedBracket(s):
        tmp = s[1:-1]
        result = ''
        for i in range(len(tmp)):
            if tmp[i] == '(':
                result += ')'
            else:
                result += '('
        return result

    def makeRightBracket(s):
        if s == "":
            return s
        u = ''
        v = ''
        for i in range(len(s) + 1):
            if len(s[:i]) != 0 and checkBalancedBracket(s[:i]):
                u = s[:i]
                v = s[i:]
                break
        if checkRightBracket(u):
            return u + makeRightBracket(v)
        else:
            return "(" + makeRightBracket(v) + ")" + reversedBracket(u)

    if p == "":
        return ""

    if checkRightBracket(p):
        return p

    answer = makeRightBracket(p)

    return answer