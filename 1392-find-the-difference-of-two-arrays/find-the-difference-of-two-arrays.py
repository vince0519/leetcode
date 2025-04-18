class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result_1, result_2 = [], []
        set_1, set_2 = set(nums1), set(nums2)

        for num in set_1:
            if num not in set_2:
                result_1.append(num)

        for num in set_2:
            if num not in set_1:
                result_2.append(num)

        return result_1, result_2

