class Solution:
    answer = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        arr = []

        def backtracking(x, y):
            if ''.join(arr) == word:
                self.answer = True
                return True
            up = (x-1, y)
            down = (x+1, y)
            right = (x, y+1)
            left = (x, y-1)
            for (x, y) in [up, down, right, left]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y] and board[x][y] == word[len(arr)]:
                    visited[x][y] = True
                    arr.append(board[x][y])
                    backtracking(x, y)
                    arr.pop()
                    visited[x][y] = False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if not self.answer and board[x][y] == word[0]:
                    arr = []
                    arr.append(board[x][y])
                    visited[x][y] = True
                    backtracking(x, y)
                    visited[x][y] = False
                elif self.answer:
                    break
            if self.answer:
                break

        return self.answer