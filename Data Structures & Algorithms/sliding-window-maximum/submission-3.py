import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left, right = 0, 0
        q = deque()
        while right < len(nums):
            q.append(nums[right])
            win_len = right - left + 1
            if win_len < k:
                right += 1
            else:
                if len(res)<=1 or nums[right] > res[-1] or nums[left-1] == res[-1]:
                    res.extend(heapq.nlargest(1, q))
                else:
                    res.append(res[-1])
                q.popleft()
                right += 1
                left += 1
        return res
