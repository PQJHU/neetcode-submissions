# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        The brutal solution would be using a new linked list and load the nodes one by one, complexity O(n^n)
        Thoughts:
        - The linked list has only one direction, you cannot traverse backwards
        - but we need to know get node n-2 after node 2. One thought would be creating a reversed linked list with O(n)
        - and then reorder the original list by linking both the original next and reversed list, O(n)
        However, by creating a reversed linked list, it would be impossible to know when to stop
        So, we need to know the middle point of the linked list
        """

        # find the middle point
        # using fast, slow pointers to split, the slow pointer will always stop at the last node of the first half
        # the fast pointer will be either the last node or the second last node

        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half linked list
        second = fast.next if fast.next else fast
        prev = None
        second_tail = slow.next
        slow.next = None # break the first
        while second_tail:
            # reverse the second part
            next = second_tail.next
            second_tail.next = prev
            prev = second_tail
            second_tail = next

        # merge the first and second half linked list one by one
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        