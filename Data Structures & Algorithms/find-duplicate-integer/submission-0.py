class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        This typical duplicate tracking without extra space algorithm is Floyd's cycle detection algo
        Two points, slow and fast, where the fast walks two steps at a time and slow walks one step at a time
        The two points will meet up in the cycle that is m steps away from the entrance point
        where m is the number of steps away from the start to entrance
        So, two phases of Floyd's cycle detection:
        1. let slow and fast points walk until they meet in the cycle
        2. reset slow to the starting point, and both pointers will walk one-step at a time until they meet again
        The meeting point is the duplicated number
        """
        slow, fast = nums[0], nums[0]
        # phase 1
        while True: # use True loop to prevent stopping at init
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0] # reset slow to starter

        # phase 2
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        