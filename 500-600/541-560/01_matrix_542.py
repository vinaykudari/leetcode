Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

---------------------------------------------------------

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h = len(mat)
        w = len(mat[0])
        ans = [[-1 for _ in range(w)] for _ in range(h)]
        q = deque()
        
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 0:
                    q.append((i, j))
                    ans[i][j] = 0
                    
        while q:
            x, y = q.popleft()
            for i, j in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                if i >= 0 and j >=0 and i < h and j < w and ans[i][j] == -1:
                    ans[i][j] = ans[x][y] + 1
                    q.append((i, j))
                
        return ans
