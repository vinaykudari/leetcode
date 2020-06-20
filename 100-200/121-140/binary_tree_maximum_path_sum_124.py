Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

------------------------------------------------------------------------------------------

# Tree - Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        def helper(root):
            nonlocal max_sum
            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            left_or_right_sum = max(max(left, right) + root.val, root.val)
            left_root_right_sum = max(left_or_right_sum, left+right+root.val)
            max_sum_at_node = max(left_or_right_sum, left_root_right_sum)
            max_sum = max(max_sum_at_node, max_sum)
                
            return left_or_right_sum
        
        helper(root)
        
        return max_sum
            
