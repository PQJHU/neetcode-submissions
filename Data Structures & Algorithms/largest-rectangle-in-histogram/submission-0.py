class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        The brutal solution is scanning all the numbers that are before and after heights[i] until the number is smaller
        than heights[i], complexity of O(n^2)

        An idea is that for each h_i, all you need to know is the nearest index that has value smaller than h_i from
        left and from right to calculate the max area for index i.
        It makes sense to reuse the algo from daily_temperature, where you need to find the nearest
        number larger than h_i. For this problem, we can try to locate the left nearest smaller height and right nearest
        smaller height for each i.
        """
        n = len(heights)
        left_nearest_idx = [-1]*n
        right_nearest_idx = [n] * n

        unresolve_idx_stack = []
        for i in range(n):
            # find nearest smaller height than heights[i]
            if not unresolve_idx_stack:
                unresolve_idx_stack.append(i)
                continue
            while unresolve_idx_stack:
                h_i = heights[i]
                target_idx = unresolve_idx_stack[-1]
                if h_i < heights[target_idx]:
                    right_nearest_idx[target_idx] = i
                    unresolve_idx_stack.pop()
                else:
                    break
            unresolve_idx_stack.append(i)

        unresolve_idx_stack = []
        for j in range(n - 1, -1, -1):
            if not unresolve_idx_stack:
                unresolve_idx_stack.append(j)
                continue
            while unresolve_idx_stack:
                h_j = heights[j]
                target_idx = unresolve_idx_stack[-1]
                if h_j < heights[target_idx]:
                    left_nearest_idx[target_idx] = j
                    unresolve_idx_stack.pop()
                else:
                    break
            unresolve_idx_stack.append(j)

        largest_areas = [heights[i] * (right_nearest_idx[i] - left_nearest_idx[i] -1) for i in range(n)]
        return max(largest_areas)
        