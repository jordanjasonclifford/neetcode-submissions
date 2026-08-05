# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # -------------------------------
        # 1. HELPER FUNCTION (DFS)
        # -------------------------------
        # each node must fall within a valid range:
        # left < node.val < right
        def valid(node, left, right):

            # -------------------------------
            # BASE CASE
            # -------------------------------
            # empty node is valid
            if not node:
                return True

            # -------------------------------
            # CHECK CURRENT NODE
            # -------------------------------
            # if node violates the BST rule → invalid
            if not (left < node.val < right):
                return False

            # -------------------------------
            # RECURSE LEFT + RIGHT
            # -------------------------------
            # left subtree:
            # values must be < current node.val
            # so update upper bound to node.val

            # right subtree:
            # values must be > current node.val
            # so update lower bound to node.val

            return (
                valid(node.left, left, node.val) and
                valid(node.right, node.val, right)
            )


        # -------------------------------
        # 2. INITIAL CALL
        # -------------------------------
        # start with full possible range
        return valid(root, float("-inf"), float("inf"))