class Solution(object):
    def calculateQuantity(self, height_l, height_r, length):
        return length * min(height_l, height_r)

    def maxArea(self, height):
        l, r = 0, len(height) - 1
        qty = 0

        while l < r:
            length = r - l
            temp_qty = self.calculateQuantity(height[l], height[r], length)
            qty = max(qty, temp_qty)  # More concise than the if block

            # Move the shorter wall inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return qty