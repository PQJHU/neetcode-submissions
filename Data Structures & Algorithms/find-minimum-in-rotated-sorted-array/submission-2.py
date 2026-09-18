class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Since we are trying to solve the problem with O(log n), it's a hint that we should use binary search
        let's say we compare the mid val to head and tail vals,
        there are a few possibilities,
        if tail val >= head val, min is head val
        else: (tail val < head val)
            if mid val >= head val, move head to mid
            if mid val <= tail val, move tail to mid
            if tail val < mid val < head val, impossible
        """
        n = len(nums)
        head, tail = 0, n -1
        while head <= tail:
            mid = (head + tail)//2
            tail_val = nums[tail]
            head_val = nums[head]
            mid_val = nums[mid]
            if tail_val >= head_val:
                # ascending order
                return head_val
            else:
                # head_val > tail_val
                if mid_val >= head_val:
                    head = mid + 1
                else:
                    # mid_val <= tail_val
                    tail = mid
        return nums[head]
        