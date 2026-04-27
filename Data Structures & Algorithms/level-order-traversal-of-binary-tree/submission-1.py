# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # -------------------------------
        # 1. EDGE CASE
        # -------------------------------
        # if tree is empty, return empty list
        if not root:
            return []

        res = []
        # final result → list of levels

        queue = deque([root])
        # queue for BFS (level-by-level traversal)


        # -------------------------------
        # 2. BFS TRAVERSAL
        # -------------------------------
        while queue:
            level = []
            # store values for current level

            # process ALL nodes currently in queue (one level)
            for _ in range(len(queue)):

                node = queue.popleft()
                # take next node from current level

                if node:
                    # add value to current level
                    level.append(node.val)

                    # push children into queue (next level)
                    queue.append(node.left)
                    queue.append(node.right)

            # only add level if it has actual values
            if level:
                res.append(level)


        # -------------------------------
        # 3. RETURN RESULT
        # -------------------------------
        return res