# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        if not head1:
            return list2
        if not head2:
            return list1

        init1, init2 = head1.val, head2.val
        if init1 > init2:
            # swap the smaller head pointer to head1
            head1, head2 = head2, head1

        while head1.next and head2:
            val1, val2 = head1.next.val, head2.val

            if val1 <= val2:
                head1 = head1.next
            else:
                temp = head1.next
                head1.next = head2
                head2 = temp

        if head2:
            head1.next = head2

        if init1 > init2:
            return list2
        else:
            return list1
