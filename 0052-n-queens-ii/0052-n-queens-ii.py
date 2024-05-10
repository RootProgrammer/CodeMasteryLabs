class Solution:
    def totalNQueens(self, n: int) -> int:
        # file=column, rank=row, empty/non-empty cell=square
        columns = set()
        upward_diagonal = set() # row+column
        downward_diagonal = set() # row-column
        result = 0

        def backtrack(row):
            # Base Case
            if row == n:
                nonlocal result
                result += 1
                return

            # Recursive Case
            for column in range(n):
                if column in columns or (row + column) in upward_diagonal or (row - column) in downward_diagonal:
                    continue

                # update for recursive call
                columns.add(column)
                upward_diagonal.add(row + column)
                downward_diagonal.add(row - column)

                backtrack(row + 1)

                # clear before next recursion
                columns.remove(column)
                upward_diagonal.remove(row + column)
                downward_diagonal.remove(row - column)

        backtrack(0)

        return result