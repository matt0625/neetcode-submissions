# we need to maintain a DLL of nodes limited by size capacity so we can have efficient access to the head and tail 
# DLL invariant is that it remains ordered with head being the least recently used element
# we also need to maintain a hashmap pointing keys to the respective node so we can have O(1) access to nodes and then extract then whenever a node is used or evicted
class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def update_value(self, newval):
        self.val = newval


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode() # real head = self.head.next
        self.tail = ListNode() # real tail = self.tail.prev
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def add(self, node):
        tail = self.tail.prev
        tail.next = node
        node.prev = tail
        node.next = self.tail
        self.tail.prev = node

    def remove_lru(self):
        lru = self.head.next
        self.head.next = lru.next
        lru.next.prev = self.head
        
        key = lru.key
        self.cache.pop(key)

    def get(self, key: int) -> int:
        # indexes to the relevant node in list and moves it to most recent pos (tail)
        if key in self.cache:
            res = self.cache[key]
            self.move_to_end(res)

            return res.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.update_value(value)
            self.move_to_end(node)

        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.add(node)

        if len(self.cache) > self.capacity:
            self.remove_lru()

        
