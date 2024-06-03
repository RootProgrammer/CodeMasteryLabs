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