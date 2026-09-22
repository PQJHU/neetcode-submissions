class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head, tail = 0, len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            mid_val, tail_val = nums[mid], nums[tail]

            if mid_val == target:
                return mid
            elif mid_val > target:
                if target < tail_val < mid_val:
                    head = mid + 1
                elif target == tail_val:
                    return tail
                else:
                    tail = mid - 1
            else:
                if mid_val < tail_val < target:
                    tail = mid - 1
                elif target == tail_val:
                    return tail
                else:
                    head = mid + 1

        return -1
  