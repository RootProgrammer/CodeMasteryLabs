class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        size = len(nums)
        current = nums[0]
        end = 0

        for index in range(1, size):
            if nums[index] < current:
                end = index
            else:
                current = nums[index]

        current = nums[-1]
        start = 0

        for index in range(size - 2, -1, -1):
            if nums[index] > current:
                start = index
            else:
                current = nums[index]

        return end - start + 1 if end != start else 0