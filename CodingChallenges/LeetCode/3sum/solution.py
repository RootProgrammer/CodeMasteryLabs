import json
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = []
        
        # Early exit if no valid triplets can exist
        if not sorted_nums or sorted_nums[0] > 0 or sorted_nums[-1] < 0:
            return []

        for i in range(len(sorted_nums) - 2):  # Adjust the loop to end sooner
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue  # Skip duplicate for i

            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    triplets.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1  # Skip duplicates for left
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1  # Skip duplicates for right
                    left += 1
                    right -= 1

        return triplets
    
# For testing
class Test:
    def compare_output(self, actual, expected):
        actual_list = json.loads(actual.replace('\'', '"'))
        expected_list = json.loads(expected)
        return actual_list == expected_list

    def test(self):
        solution = Solution()
        with open('input.txt', 'r') as input_file, open('output.txt', 'r') as output_file:
            for input_line, expected_output_line in zip(input_file, output_file):
                nums = list(map(int, input_line.strip().split(',')))
                actual_output = solution.threeSum(nums)
                actual_output_str = json.dumps(sorted(actual_output))  # Sorting to ensure consistent order
                expected_output_str = expected_output_line.strip()
                if self.compare_output(actual_output_str, expected_output_str):
                    print("Passed")
                else:
                    print("Failed")
                    print(f"Input: {nums}\nExpected: {expected_output_str}\nActual: {actual_output_str}\n")

if __name__ == "__main__":
    test_code = Test()
    test_code.test()