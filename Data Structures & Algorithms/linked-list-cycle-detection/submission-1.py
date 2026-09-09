# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's cycle detection algo
        two pointers, fast and slow, the fast one will move two steps at a time and the slow one moves one step
        stop when fast.val = slow.val, a cycle is detected, return True
        stop when fast or slow is None, return False
        """
        slow = head
        fast = head
        while slow and fast:
            if fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
        return False
