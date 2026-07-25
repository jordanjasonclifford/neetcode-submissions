# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []
        # this will store values in sorted order (because BST)


        # -------------------------------
        # 1. INORDER DFS
        # -------------------------------
        # inorder traversal of BST gives sorted values:
        # left → node → right
        def dfs(root):

            # base case: no node
            if not root:
                return

            # go left (smaller values)
            dfs(root.left)

            # process current node
            arr.append(root.val)

            # go right (larger values)
            dfs(root.right)


        # run DFS
        dfs(root)


        # -------------------------------
        # 2. RETURN KTH SMALLEST
        # -------------------------------
        # array is sorted, so kth smallest is at index k-1
        return arr[k - 1]
