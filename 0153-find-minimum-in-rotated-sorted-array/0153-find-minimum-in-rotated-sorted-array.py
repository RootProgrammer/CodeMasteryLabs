class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0] # left most
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            median = (left + right) // 2
            result = min(result, nums[median])

            # looking for correct portion
            if nums[median] >= nums[left]:
                left = median + 1
            else:
                right = median - 1

        return result