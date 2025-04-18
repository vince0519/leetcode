class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        l, r = 0, 0
        non_zero_count = 0

        while r < len(nums):
            if nums[r] != 1:
                non_zero_count += 1

            if non_zero_count > 1:
                while non_zero_count > 1:
                    if nums[l] != 1:
                        non_zero_count -= 1
                    l += 1

            result = max(result, r-l)
            r += 1

        return result