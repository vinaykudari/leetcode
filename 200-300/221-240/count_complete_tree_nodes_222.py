Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

---------------------------Tree-Recursion---------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(root):
            if root is None:
                return 0
            return 1 + height(root.left)
        
        if not root:
            return 0
            
        height_of_left_subtree = height(root.left)
        height_of_right_subtree = height(root.right)
        
        if height_of_left_subtree == height_of_right_subtree:
            return 2 ** height_of_left_subtree + self.countNodes(root.right)
        else:
            return 2 ** height_of_right_subtree + self.countNodes(root.left)
        
#         count = 0
#         def helper(root):
#             nonlocal count
#             if root is None:
#                 count += 1
#                 return 
#             helper(root.right)
#             helper(root.left)
#             return count
        
#         if root is None:
#             return 0 
        
#         return helper(root) - 1
        
