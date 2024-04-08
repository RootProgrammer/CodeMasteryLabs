from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = []

        for i in range(len(sorted_nums)):
            if i>0 and sorted_nums[i]==sorted_nums[i-1]:
                continue

            left, right = i+1, len(sorted_nums)-1
            
            while left<right:
                current_sum=sorted_nums[i]+sorted_nums[left]+sorted_nums[right]

                if current_sum<0:
                    left+=1
                elif current_sum>0:
                    right-=1
                else:
                    triplets.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1
                    while left<right and sorted_nums[left]==sorted_nums[left-1]:
                        left+=1
                    while left<right and sorted_nums[right]==sorted_nums[right+1]:
                        right-=1

        return triplets
    
# For testing
if __name__ == "__main__":
    solution = Solution()
    with open('input.txt', 'r') as file:
        for line in file:
            nums = list(map(int, line.strip().split(',')))  # Convert the line into a list of integers
            triplets = solution.threeSum(nums)  # Find the triplets for the current list of numbers
            print(f"Input: {nums}\nTriplets: {triplets}\n")  # Print the input and the found triplets

