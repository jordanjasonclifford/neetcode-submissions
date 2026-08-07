# Definition for a Node.
# class Node:
#     def __init__(
#         self,
#         x: int,
#         next: 'Node' = None,
#         random: 'Node' = None
#     ):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(
        self,
        head: 'Optional[Node]'
    ) -> 'Optional[Node]':

        # Map each original node to its copied node.
        #
        # None maps to None so we can safely handle
        # nodes whose next or random pointer is None.
        old_to_copy = {None: None}


        # -------------------------------
        # 1. CREATE A COPY OF EVERY NODE
        # -------------------------------
        # First pass:
        # create each copied node without connecting
        # its next or random pointers yet.
        current = head

        while current:
            # Create a new node with the same value
            copied_node = Node(current.val)

            # Store the relationship:
            # original node -> copied node
            old_to_copy[current] = copied_node

            # Move through the original list
            current = current.next


        # -------------------------------
        # 2. CONNECT NEXT AND RANDOM POINTERS
        # -------------------------------
        # Second pass:
        # use the dictionary to connect each copied node
        # to the copied versions of its neighbors.
        current = head

        while current:
            # Get the copied version of the current node
            copied_node = old_to_copy[current]

            # Point the copied node's next pointer
            # to the copy of the original next node
            copied_node.next = old_to_copy[current.next]

            # Point the copied node's random pointer
            # to the copy of the original random node
            copied_node.random = old_to_copy[current.random]

            # Move through the original list
            current = current.next


        # -------------------------------
        # 3. RETURN COPIED HEAD
        # -------------------------------
        # Return the copied version of the original head
        return old_to_copy[head]