# Link: https://leetcode.com/problems/lru-cache/

"""
    @question:
        Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

        Implement the LRUCache class:

        LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        int get(int key) Return the value of the key if the key exists, otherwise return -1.
        void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        The functions get and put must each run in O(1) average time complexity.

        ======================================================
        ======================================================

        Example 1:
            Input
                ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
                [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
            Output
                [null, null, null, 1, null, -1, null, -1, 3, 4]

            Explanation
                LRUCache lRUCache = new LRUCache(2);
                lRUCache.put(1, 1); // cache is {1=1}
                lRUCache.put(2, 2); // cache is {1=1, 2=2}
                lRUCache.get(1);    // return 1
                lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
                lRUCache.get(2);    // returns -1 (not found)
                lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
                lRUCache.get(1);    // return -1 (not found)
                lRUCache.get(3);    // return 3
                lRUCache.get(4);    // return 4
        
    ======================================================
    ======================================================
                
        Constraints:
            1 <= capacity <= 3000
            0 <= key <= 104
            0 <= value <= 105
            At most 2 * 105 calls will be made to get and put.
"""

class LRUCache:

    class Node:
        
        def __init__(self):
            self.val = None
            self.next = None
            self.prev = None
            self.key = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.sz = 0
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            val = node.val
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = self.head.next
            node.next.prev = node
            node.prev = self.head
            self.head.next = node

            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            node.key = key
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = self.head.next
            node.next.prev = node
            node.prev = self.head
            self.head.next = node
        else:
            if self.sz == self.capacity:
                del self.map[self.tail.prev.key]
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                self.sz -= 1
            node = self.Node()
            node.val = value
            node.key = key
            self.map[key] = node
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            self.sz += 1

