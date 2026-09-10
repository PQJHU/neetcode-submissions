class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        The most intuitive thought would be using two pointer, left and right
        init: left = 0, right = n-1, compute the area
        while left < right,
        if left value <  right value, left++,
        elif left value > right value, right--,
        else left ++, right --
        compute the area
        as we shrink the bottom length, we are looking for higher bar to replace the lower one
        """
        n= len(heights)
        left, right = 0, n-1
        max_area = 0
        while left < right:
            left_val = heights[left]
            right_val = heights[right]
            area = (right - left) * min(right_val, left_val)
            max_area = max(max_area, area)
            if left_val <= right_val:
                left += 1
            if left_val >= right_val:
                right -= 1
        return max_area
        