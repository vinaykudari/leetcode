# Tree - Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def recur(root, val):
            if root is None:
                return None
            
            elif root.val == val:
                return root
            
            elif root.left and val < root.val:
                return recur(root.left, val)
                
            elif root.right and val > root.val:
                return recur(root.right, val)
                
        return recur(root, val)
            
            
            
