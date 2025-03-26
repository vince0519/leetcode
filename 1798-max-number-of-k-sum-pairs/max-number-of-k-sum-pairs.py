class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_dict = {}
        operation_count = 0

        for num in nums:
            diff = k - num
            if nums_dict.get(diff, 0) > 0:
                operation_count += 1
                nums_dict[diff] -= 1
            else:
                nums_dict[num] = nums_dict.get(num, 0) + 1

        return operation_count