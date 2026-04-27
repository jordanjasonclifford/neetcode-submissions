# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # -------------------------------
        # 1. START AT ROOT
        # -------------------------------
        # we will traverse down the tree
        curr = root


        # -------------------------------
        # 2. TRAVERSE THE TREE
        # -------------------------------
        # use BST property:
        # left subtree < node < right subtree

        while curr:

            # -------------------------------
            # 3. BOTH NODES ON RIGHT SIDE
            # -------------------------------
            # if both p and q are greater than current node,
            # LCA must be in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # -------------------------------
            # 4. BOTH NODES ON LEFT SIDE
            # -------------------------------
            # if both p and q are smaller than current node,
            # LCA must be in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # -------------------------------
            # 5. SPLIT POINT → THIS IS LCA
            # -------------------------------
            # if one node is on the left and the other is on the right,
            # OR one of them equals curr,
            # then current node is the lowest common ancestor
            else:
                return curr