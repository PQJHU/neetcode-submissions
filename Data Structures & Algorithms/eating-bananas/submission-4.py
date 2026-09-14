class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles = sorted(piles)
        head, tail = 0, n - 1
        while head < tail:
            mid = (head + tail) // 2
            k = piles[mid]
            hours = mid + 1 + sum([-(-pile // k) for pile in piles[mid + 1 :]])
            if hours > h:
                head = mid + 1
            elif hours < h:
                tail = mid
            else:
                return piles[mid]
        # piles[head] satisfy the h goal, but it's only the upper bound
        upper = piles[head]
        lower = piles[head-1] if head >0 else 1
        while lower < upper:
            mid = (upper + lower)//2  # half the speed
            mid_hours = head + sum([-(-pile // mid) for pile in piles[head:]])
            if mid_hours > h:
                lower = mid + 1
            elif mid_hours <= h:
                upper = mid
        return lower
