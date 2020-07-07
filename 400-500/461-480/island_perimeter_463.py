You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

-------------Tried-via-DFS-can-be-done-with-2-loops-------------

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        def dfs(grid, x, y, grid_len, grid_width):
            nonlocal perimeter
            if x < 0 or y < 0 or x >= grid_len or y >= grid_width or grid[x][y] == -1 or grid[x][y] == 0:
                
                return
            
            # marking the cell as visited
            grid[x][y] = -1
            
            if x == 0:
                perimeter += 1
                
            if x == grid_len-1:
                perimeter += 1
                
            if y == 0:
                perimeter += 1
                
            if y == grid_width-1:
                perimeter += 1
            
            if x < grid_len-1 and grid[x+1][y] == 0:
                perimeter += 1
                
            if y < grid_width-1 and grid[x][y+1] == 0:
                perimeter += 1
                
            if x > 0 and grid[x-1][y] == 0:
                perimeter += 1
                
            if y > 0 and grid[x][y-1] == 0:
                perimeter += 1
                
            dfs(grid, x+1, y, grid_len, grid_width)
            dfs(grid, x, y+1, grid_len, grid_width)
            dfs(grid, x-1, y, grid_len, grid_width)
            dfs(grid, x, y-1, grid_len, grid_width)
            
        grid_len = len(grid)
        grid_width = len(grid[0])
        for i in range(grid_len):
            for j in range(grid_width):
                if grid[i][j] == 1:
                    dfs(grid, i, j, grid_len, grid_width)
                    return perimeter
        
