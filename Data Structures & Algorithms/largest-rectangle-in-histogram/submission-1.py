class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        A more clever solution can be passing through the list one time. same idea different implementation
        The unresolved stack essentially records the monotonic non-decreasing heights
        For each time a value pops out from the stack, this popped out index found both
            1. the nearest right index, which is i
            2. the nearest left index, which is new top stack index

        Another clear tricky to pop out all the indices left in the stack is by appending 0 by the end of heights
        when the iteration reaches the end, value 0 will pop out all the indices left in the stack and record the right
        nearest index of n
        """
        unresolved_stack = []
        max_area = 0
        heights.append(0)

        for i, h_i in enumerate(heights):

            while unresolved_stack and h_i < heights[unresolved_stack[-1]]:
                right_idx = i
                popped_idx = unresolved_stack.pop()
                left_idx = unresolved_stack[-1] if unresolved_stack else -1
                # new top stack, if stack is empty, left nearest will be -1
                _area_i = heights[popped_idx] * (right_idx - left_idx -1)
                max_area = max(max_area, _area_i)

            unresolved_stack.append(i)

        return max_area
        