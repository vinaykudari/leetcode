Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

-------------------------------BFS-Tree-------------------------------

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return 
        
        res = [[root.val]]
        bfs = deque([root])
        
        while bfs:
            connected_nodes = []
            while bfs:
                node = bfs.popleft()
                if node.left:
                    connected_nodes.append(node.left)
                if node.right:
                    connected_nodes.append(node.right)
            
            for _ in connected_nodes:
                bfs.append(_)
            res.append([node.val for node in connected_nodes])
                
        return res[:-1][::-1]
