class Node:
    def __init__(self, key, val):
        # Store both the key and value.
        #
        # The key is needed when we evict a node from the linked list,
        # because we must also delete that same key from the dictionary.
        self.key = key
        self.val = val

        # References to the previous and next nodes in the doubly linked list.
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Maximum number of key-value pairs the cache can hold.
        self.cap = capacity

        # Dictionary mapping:
        # key -> Node object
        #
        # This gives us O(1) access to any cached item.
        self.cache = {}

        # Create two dummy, or sentinel, nodes.
        #
        # left represents the least recently used side.
        # right represents the most recently used side.
        #
        # Actual cache nodes will always be placed between these two.
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Initially, the linked list is empty:
        #
        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """
        Remove an existing node from the doubly linked list.

        This does not remove the node from the dictionary.
        It only disconnects the node from the linked list.
        """

        # Save the nodes immediately before and after this node.
        prev_node = node.prev
        next_node = node.next

        # Connect the previous node directly to the next node,
        # skipping over the node being removed.
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        """
        Insert a node directly before the right sentinel.

        Because the right side represents the most recently used side,
        inserting here marks the node as the most recently used item.
        """

        # The current most recently used node is right.prev.
        previous_mru = self.right.prev

        # Insert the new node between previous_mru and right.
        #
        # Before:
        # previous_mru <-> right
        #
        # After:
        # previous_mru <-> node <-> right
        previous_mru.next = node
        node.prev = previous_mru

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        """
        Return the value associated with key.

        If the key exists, mark it as the most recently used item.
        If the key does not exist, return -1.
        """

        if key in self.cache:
            # Retrieve the node from the dictionary in O(1) time.
            node = self.cache[key]

            # The item was just accessed, so it is now the most recently used.
            #
            # First remove it from its current linked-list position.
            self.remove(node)

            # Then insert it at the right side of the list.
            self.insert(node)

            # Return the stored value.
            return node.val

        # The key is not currently stored in the cache.
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair.

        The inserted or updated key becomes the most recently used item.
        If the cache exceeds capacity, remove the least recently used item.
        """

        if key in self.cache:
            # The key already exists.
            #
            # Remove its old node from the linked list before replacing it.
            # Otherwise, the old node would remain in the list even though
            # the dictionary points to a new node.
            old_node = self.cache[key]
            self.remove(old_node)

        # Create a new node containing the updated key and value.
        new_node = Node(key, value)

        # Store the new node in the dictionary.
        #
        # If the key already existed, this overwrites the dictionary's
        # reference to the old node.
        self.cache[key] = new_node

        # Place the node at the most recently used side.
        self.insert(new_node)

        # If adding this item caused the cache to exceed its capacity,
        # evict the least recently used item.
        if len(self.cache) > self.cap:
            # The node immediately after left is always the least
            # recently used real node.
            lru_node = self.left.next

            # Remove the least recently used node from the linked list.
            self.remove(lru_node)

            # Also remove its key from the dictionary.
            del self.cache[lru_node.key]