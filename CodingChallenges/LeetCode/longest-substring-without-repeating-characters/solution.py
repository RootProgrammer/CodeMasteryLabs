class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        # Check for empty string
        if not s:
            return 0

        for right in range(len(s)):
            # Continue to slide the window if duplicate is found
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            # Update max_length after ensuring s[right] is added to the set
            max_length = max(max_length, right - left + 1)

        return max_length

# For testing
class Test:
    def test(self):
        solution = Solution()
        with open('input.txt', 'r') as input_file, open('output.txt', 'r') as output_file:
            passed = True
            for input_line, expected_output_line in zip(input_file, output_file):
                input_str = input_line.strip()
                expected_output = int(expected_output_line.strip())  # Expected output is an integer
                actual_output = solution.lengthOfLongestSubstring(input_str)
                if actual_output == expected_output:
                    print(f"Passed: {input_str} -> {actual_output}")
                else:
                    print(f"Failed: {input_str} -> {actual_output} (Expected: {expected_output})")
                    passed = False
            if passed:
                print("All test cases passed!")
            else:
                print("Some test cases failed.")

if __name__ == "__main__":
    test_code = Test()
    test_code.test()
