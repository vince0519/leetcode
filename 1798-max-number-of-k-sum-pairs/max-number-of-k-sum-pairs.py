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
            if nums_dict.get(diff, 1) <= 0:
                nums_dict[diff] += 1
                operation_count += 1
            else:
                if nums_dict.get(num) != None:
                    nums_dict[num] -= 1
                else:
                    nums_dict[num] = 0

        return operation_count