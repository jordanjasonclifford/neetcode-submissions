# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # -------------------------------
        # BASE CASE
        # -------------------------------
        # if node doesn't exist, depth = 0
        if not root:
            return 0

        # -------------------------------
        # RECURSE LEFT + RIGHT
        # -------------------------------
        # get depth of left subtree
        left = self.maxDepth(root.left)

        # get depth of right subtree
        right = self.maxDepth(root.right)

        # -------------------------------
        # RETURN RESULT
        # -------------------------------
        # current depth = 1 (this node) + deeper side
        return 1 + max(left, right)