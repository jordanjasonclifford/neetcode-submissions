"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        # edge case: if graph is empty
        if not node:
            return None

        # hashmap to map original nodes → cloned nodes
        # this prevents duplicate copies and handles cycles
        oldToNew = {}

        def dfs(curr):
            # if we’ve already cloned this node, just return it
            # this avoids infinite loops in cyclic graphs
            if curr in oldToNew:
                return oldToNew[curr]

            # create a copy of the current node
            copy = Node(curr.val)

            # store it in the hashmap BEFORE exploring neighbors
            # this is important for handling cycles correctly
            oldToNew[curr] = copy

            # go through all neighbors of current node
            for nei in curr.neighbors:

                # recursively clone neighbors and attach them
                copy.neighbors.append(dfs(nei))

            # return the fully built clone node
            return copy

        # start DFS from the given node
        return dfs(node)