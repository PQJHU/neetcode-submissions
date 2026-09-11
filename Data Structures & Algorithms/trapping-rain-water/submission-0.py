class Solution:
    def trap(self, height: List[int]) -> int:
        """
        For each i, the water trapped is determined by the highest bar to its left and highest bar to its right
        max(min(left_highest, right_highest) - height[i], 0)
        we can have two lists that contain the highest bar to the left and highest bar to the right
        """
        water_trapped = 0
        left_highest = []
        right_highest = []
        l_h = 0
        for i in range(len(height)):
            left_highest.append(l_h)
            l_h = max(height[i], l_h)
        r_h = 0
        for j in range(len(height)-1, -1, -1):
            right_highest.append(r_h)
            r_h = max(height[j], r_h)
        right_highest.reverse()

        for k in range(len(height)):
            water_trapped += max(min(left_highest[k], right_highest[k]) - height[k], 0)

        return water_trapped
        