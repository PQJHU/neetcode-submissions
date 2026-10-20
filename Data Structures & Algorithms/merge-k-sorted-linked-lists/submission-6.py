# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_head = ListNode(val=-10_001)
        tail = res_head

        while lists:

            if lists[0] is None:
                lists.pop(0)
                continue

            _min_node = ListNode(val=10_001)
            _min_idx = 0
            for i in range(len(lists)):
                ll = lists[i]
                if ll is not None:
                    if ll.val < _min_node.val:
                        _min_node = ll
                        _min_idx = i
                    if ll.val == tail.val:
                        _min_node = ll
                        _min_idx = i
                        break # early break

            tail.next = _min_node
            lists[_min_idx] = _min_node.next
            if not _min_node.next:
                lists.pop(_min_idx)
            tail = tail.next
        return res_head.next
