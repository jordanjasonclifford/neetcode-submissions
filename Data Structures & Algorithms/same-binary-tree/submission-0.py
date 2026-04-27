# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # -------------------------------
        # 1. BASE CASE: BOTH ARE NONE
        # -------------------------------
        # if both nodes are None, they match
        # (we reached the end of both trees at the same time)
        if not p and not q:
            return True


        # -------------------------------
        # 2. CHECK IF CURRENT NODES MATCH
        # -------------------------------
        # both nodes must exist AND have same value
        if p and q and p.val == q.val:

            # recursively check:
            # left subtree AND right subtree must both match
            return (
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)
            )


        # -------------------------------
        # 3. OTHERWISE → NOT THE SAME
        # -------------------------------
        # cases:
        # - one node is None, the other isn't
        # - values don't match
        else:
            return False


        