class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #k = max_0
        curr_zero = 0
        ans = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                curr_zero += 1
                
            while curr_zero > k:
                if nums[l] == 0:
                    curr_zero -= 1
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans
            