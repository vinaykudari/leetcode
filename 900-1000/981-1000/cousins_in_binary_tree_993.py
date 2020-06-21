In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

-----------------------------------------Tree-Recursion-----------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def get_height_and_parent(root, val, height, parent):
            if root is not None:
                if root.val == val:
                    return height, parent.val

                height_and_parent = get_height_and_parent(root.right, val, height+1, root)
                if height_and_parent:
                    return height_and_parent
                height_and_parent = get_height_and_parent(root.left, val, height+1, root)
                
                return height_and_parent
                
                
        n1 = get_height_and_parent(root, x, 0, root)
        n2 = get_height_and_parent(root, y, 0, root)
        
        if (n1 and n2) and (n1[0] == n2[0]) and (n1[1] != n2[1]):
            return True
        
        return False
        
