"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None 

        copy_head = Node(head.val, None, None)

        # both starts from head node
        orig_next = head
        copy_next = copy_head
        node_records = {head: copy_head}

        # copy the next chain of linked list
        while orig_next.next:
            orig_next = orig_next.next # +1 at original list
            copy_next.next = Node(orig_next.val, None, None)
            copy_next = copy_next.next
            node_records[orig_next] = copy_next
        # copy the last not None node
        # copy_next.next = Node(orig_next.val, None, None)
        # node_records[orig_next] = copy_next.next

        # copy the random chain
        orig_next = head
        copy_next = copy_head

        while orig_next:
            rnd_node = orig_next.random
            if rnd_node is None:
                copy_next.random = None
            else:
                copy_next.random = node_records[rnd_node]
            orig_next = orig_next.next
            copy_next = copy_next.next

        return copy_head
