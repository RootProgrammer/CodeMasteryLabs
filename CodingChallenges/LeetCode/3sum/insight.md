# [15. 3Sum](https://leetcode.com/problems/3sum/description/)

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Example 1

- Input: nums = [-1,0,1,2,-1,-4]
- Output: [[-1,-1,2],[-1,0,1]]
- Explanation:
  - nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
  - nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
  - nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
  - The distinct triplets are [-1,0,1] and [-1,-1,2].
  - Notice that the order of the output and the order of the triplets does not matter.

### Example 2

- Input: nums = [0,1,1]
- Output: []
- Explanation: The only possible triplet does not sum up to 0.

### Example 3

- Input: nums = [0,0,0]
- Output: [[0,0,0]]
- Explanation: The only possible triplet sums up to 0.

### Constraints

- `3 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`

## Problem Breakdown

The 3Sum problem requires finding all unique triplets in a given array that sum up to zero. The challenge lies not only in identifying these triplets but also in ensuring that the solution does not include duplicates and is efficient in terms of time and space complexity.

### Strategy Followed

- **Sorting:** The initial step involved sorting the array. This simplification allowed for the effective application of a two-pointer technique.
- **Two-Pointer Technique:** To find triplets, we iterated through the array, using each element as a potential first element of the triplet and applying the two-pointer technique to find two other elements that, together, sum up to zero.
- **Skipping Duplicates:** A critical part of the strategy was to implement checks to skip over duplicate elements, ensuring the uniqueness of each triplet.

### Applied Data Structure and Algorithm

- **Data Structure:** The primary data structure used was a simple array for storing numbers and triplets. The choice of data structure was guided by the need for efficient access and iteration.
- **Algorithm:** The solution chiefly relies on sorting and the two-pointer technique. Sorting the array initially allows us to apply the two-pointer method effectively, reducing the problem's complexity from O(n^2) to near-linear for finding the triplets.

### What We've Learned

- **Efficiency through Sorting:** Sorting can significantly simplify certain problems, making them more tractable by bringing elements into a predictable order.
- **Eliminating Duplicates:** When a problem requires unique solutions, careful consideration must be given to how duplicates can be identified and skipped without excessively complicating the solution or compromising efficiency.
- **Importance of Edge Cases:** Handling edge cases, such as arrays with insufficient elements or arrays with all elements being the same, is crucial for a robust solution.

### Key Notes

- **Early Exit Conditions:** Implementing conditions that allow for early exits when certain criteria are met can further optimize the solution.
- **Readability vs. Optimization:** Striking the right balance between code readability and optimization is essential. While optimizations can improve efficiency, they should not overly complicate the solution to the detriment of readability and maintainability.
- **Iterative Testing:** Incrementally testing the solution with various test cases, including edge cases, is vital for ensuring the solution's correctness and robustness.

---
