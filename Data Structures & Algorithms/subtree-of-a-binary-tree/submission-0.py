# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # -------------------------------
        # 1. EDGE CASES
        # -------------------------------
        # if subRoot is empty, it's always a subtree
        if not subRoot:
            return True

        # if main tree is empty but subRoot isn't → impossible
        if not root:
            return False


        # -------------------------------
        # 2. CHECK IF TREES MATCH HERE
        # -------------------------------
        # if the current root matches subRoot exactly
        if self.sameTree(root, subRoot):
            return True


        # -------------------------------
        # 3. RECURSE LEFT + RIGHT
        # -------------------------------
        # otherwise, check if subRoot exists in left OR right subtree
        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )


    def sameTree(self, s, t):
        # -------------------------------
        # 1. BOTH NULL → MATCH
        # -------------------------------
        if not s and not t:
            return True

        # -------------------------------
        # 2. CHECK CURRENT NODE MATCH
        # -------------------------------
        if s and t and s.val == t.val:
            return (
                self.sameTree(s.left, t.left) and
                self.sameTree(s.right, t.right)    
            )

        # -------------------------------
        # 3. OTHERWISE → NOT MATCH
        # -------------------------------
        return False