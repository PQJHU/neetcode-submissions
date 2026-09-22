class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        