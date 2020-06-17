# Question
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

# Graph - DFS

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x, y, board_len, board_width):
            if x >= board_len or y >= board_width or board[x][y] == 'X' or x < 0 or y < 0 or board[x][y] == 'V':
                return
            
            if board[x][y] == 'O':
                board[x][y] = 'Z'
            else:
                board[x][y] = 'V'
                
            dfs(x+1, y, board_len, board_width)
            dfs(x-1, y, board_len, board_width)
            dfs(x, y+1, board_len, board_width)
            dfs(x, y-1, board_len, board_width)
            
        if not board:
            return
        
        board_len, board_width = len(board), len(board[0])
        
        if board_len <= 2 or board_width <= 2:
            return
        
        for j in range(board_width):
            if board[0][j] == 'O':
                dfs(0, j, board_len, board_width)

        for j in range(board_width):
            if board[board_len-1][j] == 'O':
                dfs(board_len-1, j, board_len, board_width)
 
        for i in range(board_len):
            if board[i][0] == 'O':
                dfs(i, 0, board_len, board_width)

        for i in range(board_len):
            if board[i][board_width-1] == 'O':
                dfs(i, board_width-1, board_len, board_width)
                
        for i in range(board_len):
            for j in range(board_width):
                if board[i][j] == 'Z' or board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
                
        
