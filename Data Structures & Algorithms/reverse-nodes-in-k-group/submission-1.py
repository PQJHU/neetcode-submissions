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
        two node pointers, group_start and next_group_start,
        and one traveling pointer, curr, starting from group_start to next_group_start

        dummy = ListNode(0, head)
        prev_group_tail = dummy # the prev_group_tail is meant to connect the groups
        # we start with the real head node
        group_start = curr = head

        find the kth node after the given group head

        if kth node is not None:
            next_group_start is the next node of kth node
            then, curr traverse left to right, reversing the next and curr node and move to the next
            while curr is not next_group_start
                next = curr.next,
                curr.next = prev
                prev = curr
                curr = next
            
            prev_group_tail.next = prev # [this is important! the curr is now pointing at next_group_start node]
            prev_group_tail = group_start
            group_start =next_group_start

        # connect the prev_group_tail with the curr, regardless if there are nodes after curr, as now curr is pointing
        as the start of the next remained group

        [LESSON LEARNED]
        - It's important to understand the reverse operation with the while-loop has 2 possible stopping states relative
        to stopping node S:
            1. stopped 1 node before node S, without flipping the node (while curr.next is not S)
            2. stopped at node S, flipping the node before S (while curr is not S)
        There is no way to stop at 1 node before S and also flipping that node
        I was struggling with prev_group_tail.next = prev/curr
        
        - Notice the solution uses next_group_start instead of group_end to separate the operation, the intuitive
        understanding is that after each loop, you want to have the pointers in the same state. 
        In this case, curr, group_start are all pointing to the start of a group.

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
