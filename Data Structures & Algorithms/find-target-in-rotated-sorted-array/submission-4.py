class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        After rotation, from 0 the until k there will be monotonic increase
        k can be 0...n-1
        and then drop to minimum, and then monotonic increase
        The key comparison should be between the mid val and target

        if mid val > target: the target can either be on the left side or on the right side of mid val
            if mid val > target > tail val: mid val is on right side of target, move tail to mid -1
            if mid val > tail val > target:  mid val is on the left side of target, move head to mid + 1
            if tail val > mid val > target: mid val is on the right side of target, move tail to mid - 1
        elif mid val < target:
            if target > mid val > tail val: target to the right of mid val, move head to mid + 1
            if target > tail val > mid val: target to the left of mid val, move tail to mid -1
            if tail val > target > mid val: target to the right of mid val, move head to mid + 1

        The case by case logic is very cumbersome, and it might not hold in edge cases
        for example [3,1], target = 1, will have to make special treatment
        """

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
  