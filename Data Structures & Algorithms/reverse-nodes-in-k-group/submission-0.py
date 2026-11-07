# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_k_node(self, head: Optional[ListNode], k:int):
        """
        Get the kth node starting from head
        Return kth node after the head if exists, including None
        """

        count = 1
        node = head
        while node:
            count += 1
            node = node.next
            if count == k:
                return node
        return None

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        two node pointers, group_start and next_group_start, and one traveling pointer, curr, starting from group_start to next_group_start
        dummy = ListNode(0, head)

        group_start = next_group_start = curr = dummy
        prev_group_tail = ListNode() # init
        move next_group_start towards right, while next_group_start.next None
        next_group_start pause after moving k+1 steps from head,
        then, curr traverse left to right, reversing the next and curr node and move to the next
            next = curr.next,
            curr.next = prev
            prev = curr
            curr = next
        until curr points 1 node before next_group_start

        prev_group_tail.next = curr
        prev_group_tail = group_start

        group_start =next_group_start = curr
        """
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        group_start = curr = head
        
        kth_node = self.get_k_node(head, k)

        while kth_node:
            next_group_start = kth_node.next
            prev = None

            while curr is not next_group_start:
                # flip nodes curr with its prev node
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            prev_group_tail.next = prev
            prev_group_tail = group_start
            group_start = next_group_start
            kth_node = self.get_k_node(next_group_start, k)

        prev_group_tail.next = curr

        return dummy.next
