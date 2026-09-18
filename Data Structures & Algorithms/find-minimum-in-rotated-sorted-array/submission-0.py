class Solution:
    def findMin(self, nums: List[int]) -> int:
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
        