class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        A more structural way of thinking is:
        the mid point will split the list by half, at least one side is fully sorted
        first find the sorted half,
        if the target falls into that half, search that part
        else search another half
        """

        head, tail = 0, len(nums) - 1

        while head <= tail:
            mid = (head + tail) // 2
            head_val, tail_val = nums[head], nums[tail]
            mid_val = nums[mid]

            if mid_val == target:
                return mid

            if mid_val >= head_val:  # left half sorted
                if head_val <= target < mid_val:
                    # target in the left half
                    tail = mid - 1
                else:
                    head = mid + 1
            else:  # right half sorted
                if mid_val < target <= tail_val:
                    head = mid + 1
                else:
                    tail = mid - 1

        return -1
        