class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track_map = {} # value : index

        for index, value in enumerate(nums):
            first_number = target - value

            if first_number in track_map:
                return [track_map[first_number], index]

            track_map[value] = index