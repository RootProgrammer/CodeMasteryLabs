class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_to_character = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(index, current_string):
            if len(current_string) == len(digits):
                result.append(current_string)

                return

            for character in digit_to_character[digits[index]]:
                backtrack(index + 1, current_string + character)

        if digits:
            backtrack(0, "")

        return result