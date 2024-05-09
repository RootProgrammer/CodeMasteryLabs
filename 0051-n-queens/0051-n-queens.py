class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # file=column, rank=row, empty/non-empty cell=square
        columns = set()
        upward_diagonal = set() # row+column
        downward_diagonal = set() # row-column
        board = [["."] * n for square in range(n)]
        result = []

        def backtrack(row):
            # Base Case
            if row == n:
                board_snap = ["".join(row) for row in board]
                result.append(board_snap)
                return

            # Recursive Case
            for column in range(n):
                if column in columns or (row + column) in upward_diagonal or (row - column) in downward_diagonal:
                    continue

                # update for recursive call
                columns.add(column)
                upward_diagonal.add(row + column)
                downward_diagonal.add(row - column)
                board[row][column] = "Q"

                backtrack(row + 1)

                # clear before next recursion
                columns.remove(column)
                upward_diagonal.remove(row + column)
                downward_diagonal.remove(row - column)
                board[row][column] = "."

        backtrack(0)

        return result