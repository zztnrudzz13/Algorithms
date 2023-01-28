class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for t in tokens:
            if t in ['*', '/', '+', '-']:
                s = stack.pop()
                f = stack.pop()
                tmp = int(eval(str(f)+t+str(s)))
                stack.append(tmp)
            else:
                stack.append(t)
        return stack[0]