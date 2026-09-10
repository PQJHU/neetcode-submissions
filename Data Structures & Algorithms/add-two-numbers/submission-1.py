# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res= ListNode(0, None)
        p1 = l1
        p2 = l2
        pr = res
        carry = 0

        while p1 or p2 or carry!= 0:
            v1 = 0 if not p1 else p1.val
            v2 = 0 if not p2 else p2.val
            _sum = v1 + v2 + carry
            pr.next = ListNode(_sum % 10, None)
            carry = _sum //10

            p1 = None if not p1 else p1.next
            p2 = None if not p2 else p2.next
            pr = pr.next

        return res.next
        