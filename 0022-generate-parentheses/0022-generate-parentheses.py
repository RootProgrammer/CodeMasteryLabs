class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_n, closed_n):
            # Base Case: If both open and closed parentheses count reach 'n',
            # then a valid combination is found, so add it to the result.
            if open_n == closed_n == n:
                result.append("".join(stack))
                return

            # Recursive Case 1: If the count of open parentheses is less than 'n',
            # add an open parenthesis to the stack and recurse with an incremented count.
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            # Recursive Case 2: If the count of closed parentheses is less than
            # the count of open parentheses, add a closed parenthesis to the stack
            # and recurse with an incremented count.
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        # Start the backtracking algorithm with counts of open and closed parentheses as 0.
        backtrack(0, 0)

        # Return the list of all valid combinations of parentheses.
        return result
