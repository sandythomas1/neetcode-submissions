class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Sentinel nodes: left = LRU, right = Most Recently Used (MRU)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node) -> None:
        """Splice node out of doubly linked list."""
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def insert(self, node: Node) -> None:
        """Insert node at right end (MRU)."""
        prev_node, next_node = self.right.prev, self.right
        prev_node.next = next_node.prev = node
        node.next, node.prev = next_node, prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Re-use existing node instead of re-instantiating
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        # New key insert
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # Evict LRU if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]