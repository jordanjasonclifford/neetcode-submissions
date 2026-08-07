class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Lets us find nodes instantly using their keys.
        self.cache = {}

        # left side = least recently used
        # right side = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Connect the nodes before and after this node.
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def insert(self, node):
        # Insert directly before the right dummy node.
        previous_node = self.right.prev

        previous_node.next = node
        node.prev = previous_node

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move it to the most recently used side.
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # Remove the old version if the key already exists.
        if key in self.cache:
            self.remove(self.cache[key])

        # Create and insert the new node.
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # Remove the least recently used item if over capacity.
        if len(self.cache) > self.capacity:
            least_recent_node = self.left.next

            self.remove(least_recent_node)
            del self.cache[least_recent_node.key]