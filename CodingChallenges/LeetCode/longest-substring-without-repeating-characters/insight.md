# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Statement

Given a string `s`, find the length of the longest **substring** (A substring is a contiguous non-empty sequence of characters within a string.) without repeating characters.

### Example 1

- Input: s = "abcabcbb"
- Output: 3
- Explanation: The answer is "abc", with the length of 3.

### Example 2

- Input: s = "bbbbb"
- Output: 1
- Explanation: The answer is "b", with the length of 1.

### Example 3

- Input: s = "pwwkew"
- Output: 3
- Explanation: The answer is "wke", with the length of 3.
- Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols, and spaces.

## Problem Breakdown

This problem is a classic example that utilizes the Sliding Window technique, which is particularly effective for challenges involving contiguous sequences of elements such as substrings or subarrays.

### Understanding the Problem

The goal is to identify the longest substring of `s` that contains no repeating characters. Key considerations include handling strings of varying lengths and compositions, from completely unique strings to those with repetitive characters.

### Edge Cases

- **Empty string**: Returns a length of 0.
- **Uniform character string**: Such as "aaaa", should return 1 because there is only one unique character.
- **All unique characters**: Returns the length of the string itself.

## Approach: Sliding Window

This technique involves two pointers to define a moving window of characters that expands and contracts based on the uniqueness of characters within it.

### Solution Explanation

- **Initialization**: Two pointers, `left` and `right`, start at the beginning of the string, with a set to track characters within the current window.
- **Expansion**: The `right` pointer moves to the right, adding new characters to the set.
- **Contraction**: When a duplicate character is found, the `left` pointer moves right until the duplicate is removed from the set, thereby making the substring unique again.
- **Tracking Maximum**: The maximum length of the substring without repeating characters is updated continuously as the window adjusts.

### Example Walkthrough

- **Input**: "abcabcbb"
  - Expands to "abc", then encounters a duplicate 'a'.
  - Contracts by moving the left pointer to just past the first 'a'.
  - Continues until the end, updating the maximum length found.

## Applied Data Structure and Algorithm

- **Data Structure**: Uses a set to efficiently check for duplicates and to quickly clear items when necessary.
- **Algorithm**: Implements the Sliding Window technique with dynamic adjustment of window boundaries based on the condition of uniqueness.

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of the string. Each character is processed at most twice (once added and once removed).
- **Space Complexity**: O(min(m, n)), where `m` is the size of the character set, and `n` is the length of the string.

## What We've Learned

- The sliding window technique is incredibly effective for problems involving substrings or subarrays where the condition of the window changes dynamically based on the sequence content.
- Using a set facilitates O(1) time complexity for adding and removing characters, making the solution efficient even for large strings.

## Key Notes

- The solution gracefully handles all types of strings by dynamically adjusting the window size.
- It’s essential to consider how the data structure used (in this case, a set) can significantly impact the efficiency of the solution.

---
