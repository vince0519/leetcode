class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result_1, result_2 = [], []
        for num in nums1:
            if num not in nums2 and num not in result_1:
                result_1.append(num)

        for num in nums2:
            if num not in nums1 and num not in result_2:
                result_2.append(num)
        
        return result_1, result_2