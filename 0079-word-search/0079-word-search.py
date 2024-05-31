from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(row, column, character_index):
            # base case: if we have found the entire word
            if character_index == len(word):
                return True

            # invalid case: out of bounds, character mismatch, or cell already visited
            if (row < 0 or column < 0 or row >= rows or column >= columns or
                word[character_index] != board[row][column] or
                (row, column) in path):
                return False

            # mark the cell as visited
            path.add((row, column))

            # recursive call: explore all four directions
            result = (
                dfs(row + 1, column, character_index + 1) or
                dfs(row - 1, column, character_index + 1) or
                dfs(row, column + 1, character_index + 1) or
                dfs(row, column - 1, character_index + 1)
            )

            # backtrack: unmark the cell as visited
            path.remove((row, column))

            return result

        # brute force: start DFS from every cell
        for row in range(rows):
            for column in range(columns):
                if dfs(row, column, 0):
                    return True

        return False
