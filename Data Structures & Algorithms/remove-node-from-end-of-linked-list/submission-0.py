# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        The core problem here is finding the nth node from the end, while we can only traverse forward
        Inspired by the previous problem, an idea is using two pointer that one is n-1 nodes ahead
        when the faster one reaches the end, the slower one is n nodes behind
        We also need to record the prev node of the slower one so that we make it point to the next of the slower one
        """

        slower, faster = head, head
        for _ in range(n-1):
            faster = faster.next

        prev = None
        while faster.next:
            prev = slower
            slower = slower.next
            faster = faster.next
        if prev:
            prev.next = slower.next
        else:
            # special case when n = size of list
            head = head.next

        return head
        