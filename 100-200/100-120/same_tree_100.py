Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

----------------Tree-Iteration---------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_tree, q_tree = [], []
        
        while True:
            while p and q:
                p_tree.append(p)
                q_tree.append(q)
                p = p.left
                q = q.left
            if not p and not q:
                if not p_tree and not q_tree:
                    return True
                p = p_tree.pop()
                q = q_tree.pop()
                if p.val != q.val:
                    return False
                p = p.right
                q = q.right
            else:
                return False
        
        return True
        
