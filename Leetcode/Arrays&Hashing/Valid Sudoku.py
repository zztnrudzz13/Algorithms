class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            visited_rows = [True] + ([False] * 9)
            visited_cols = [True] + ([False] * 9)
            for j in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if visited_rows[num]:
                        return False
                    else:
                        visited_rows[num] = True

                if board[j][i].isdigit():
                    num = int(board[j][i])
                    if visited_cols[num]:
                        return False
                    else:
                        visited_cols[num] = True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = []
                arr = [fields[j:j + 3] for fields in board[i:i + 3]]
                for j in range(len(arr)):
                    for k in range(len(arr)):
                        if arr[j][k].isdigit():
                            num = int(arr[j][k])
                            if num in tmp:
                                return False
                            else:
                                tmp.append(num)

        return True