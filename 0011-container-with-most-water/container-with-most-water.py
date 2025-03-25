class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        qty = 0

        while l < r:
            currentArea = min(height[l], height[r]) * (r - l)
            qty = max(qty, currentArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return qty