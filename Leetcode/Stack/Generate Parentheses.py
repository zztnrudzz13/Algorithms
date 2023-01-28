class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        visited = {
            '(': n - 1,
            ')': n - 1
        }
        answer = []
        real_answer = []
        arr = ['(', ')']

        s = []

        def check(sample):
            stack = []
            for p in sample:
                if p == '(':
                    stack.append('(')
                else:
                    if len(stack) != 0:
                        stack.pop()
                    else:
                        return False
            if len(stack) != 0:
                return False
            else:
                return True

        def dfs():
            if len(s) == (n - 1) * 2:
                tmp = '(' + ''.join(s) + ')'
                answer.append(tmp)
            for p in arr:
                if visited[p] != 0:
                    s.append(p)
                    visited[p] -= 1
                    dfs()
                    s.pop()
                    visited[p] += 1

        dfs()

        for s in answer:
            if check(s):
                real_answer.append(s)

        return real_answer