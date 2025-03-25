class Solution(object):
    def calculateQuantity(self, height_l, height_r, length):
        return length * min(height_l, height_r)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, qty = 0, len(height)-1, 0
        qty = 0

        while l < r:
            length = r - l
            temp_qty = self.calculateQuantity(height[l], height[r], length)
            if (temp_qty >= qty):
                qty = temp_qty

            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        return qty

        