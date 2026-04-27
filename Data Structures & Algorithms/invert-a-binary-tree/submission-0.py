# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # -------------------------------
        # 1. BASE CASE
        # -------------------------------
        # if the node doesn't exist, nothing to invert
        # this also stops recursion at leaf nodes
        if not root:
            return None


        # -------------------------------
        # 2. SWAP CHILDREN
        # -------------------------------
        # we need to swap left and right children
        # BUT we must store one side first before overwriting

        tmp = root.left
        # save original left child

        root.left = root.right
        # move right child to left

        root.right = tmp
        # move original left child to right


        # -------------------------------
        # 3. RECURSE ON BOTH SIDES
        # -------------------------------
        # after swapping current node,
        # recursively invert the left and right subtrees

        self.invertTree(root.left)
        self.invertTree(root.right)


        # -------------------------------
        # 4. RETURN ROOT
        # -------------------------------
        # return the root of the inverted tree
        return root