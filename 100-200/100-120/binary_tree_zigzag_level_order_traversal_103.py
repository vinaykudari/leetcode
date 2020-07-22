Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

-----------------------------Tree-BFS---------------------------------

from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        
        tree = deque([(root, 0)])
        res_map = defaultdict(list)
        res = []
        while tree:
            u = tree.popleft()
            if u[0].left:
                tree.append((u[0].left, u[1]+1))
            if u[0].right:
                tree.append((u[0].right, u[1]+1))
            res_map[u[1]].append(u[0].val)
        
        for i in range(u[1]+1):
            if i % 2 != 0:
                res.append(res_map[i][::-1])
            else:
                res.append(res_map[i])
        
        return res
