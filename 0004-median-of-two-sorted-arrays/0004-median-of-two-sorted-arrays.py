class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(big) < len(small):
            small, big = big, small

        left, right = 0, len(small) - 1

        while True:
            # getting median index of both arrays
            small_median = (left + right) //2
            big_median = half - small_median - 2 # 2 is for balancing two zero indexes

            small_left = small[small_median] if small_median >= 0 else float("-infinity")
            big_left = big[big_median] if big_median >= 0 else float("-infinity")
            
            small_right = small[small_median + 1] if (small_median + 1) < len(small) else float("infinity")
            big_right = big[big_median + 1] if (big_median + 1) < len(big) else float("infinity")

            # partiton is correct
            if small_left <= big_right and big_left <= small_right:
                # odd
                if total % 2:
                    return min(small_right, big_right)

                # even
                return (max(small_left, big_left) + min(small_right, big_right)) / 2
            elif small_left > big_right:
                right = small_median - 1
            else:
                left = small_median + 1
