class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, len(nums)-1
        operation_count = 0

        while l < r:
            pointer_sum = nums[l] + nums[r]

            if pointer_sum < k:
                l += 1

            elif pointer_sum > k:
                r -= 1

            else:
                operation_count += 1
                l += 1
                r -= 1

        return operation_count