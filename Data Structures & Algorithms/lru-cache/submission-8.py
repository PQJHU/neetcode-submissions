class Node:

    def __init__(self, key= None, val = None, prev: 'Node|None' = None, next: 'Node|None' = None):
        self.key = key # used to reversely remove the node from cache
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:


    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = dict()
        self.dl_head, self.dl_tail = Node(), Node() # head and tail nodes are empty nodes
        self.capacity = capacity
        self.dl_head.next, self.dl_tail.prev = self.dl_tail, self.dl_head # link head and tail

    def _remove_node(self, node: Node):
        """
        Remove the node from the double linked list
        """
        # connect prev and next nodes
        _prev = node.prev
        _next = node.next

        _prev.next = _next
        _next.prev = _prev

    def _append_node(self, node: Node):
        """
        Operation to append a node before the tail, still have head and tail sentinel
        """
        # insert the node between the tail and tail.prev
        self.dl_tail.prev.next = node
        node.prev = self.dl_tail.prev
        node.next = self.dl_tail
        self.dl_tail.prev = node
        self.dl_tail.next = None

    def get(self, key: int) -> int:
        """
        Using Double-end queue to refresh the most recent used item
        """
        if key not in self.cache:
            return -1
        _node = self.cache[key]
        val = _node.val
        self._remove_node(_node)
        self._append_node(_node)
        return val

    def put(self, key: int, value: int) -> None:
        """
        O(1)
        """
        if key in self.cache:
            # existed key, update val, move node to the end of list, connect the prev and next
            _node = self.cache[key]
            _node.val = value  # update val
            self._remove_node(_node)
            self._append_node(_node)
        else:
            # new key, create node
            _new_node = Node(key, value)
            self._append_node(_new_node)
            self.cache[key] = _new_node

        # remove node from head and cache
        if len(self.cache) > self.capacity:
            _head_node = self.dl_head.next
            self._remove_node(_head_node)
            self.cache.pop(_head_node.key)

