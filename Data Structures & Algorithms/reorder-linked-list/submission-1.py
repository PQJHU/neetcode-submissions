# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half linked list
        prev = None
        second_tail = slow.next
        slow.next = None # break the first
        while second_tail:
            # reverse the second_tail part
            next = second_tail.next
            second_tail.next = prev
            prev = second_tail
            second_tail = next

        # merge the first and second half linked list one by one
        second = prev
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

