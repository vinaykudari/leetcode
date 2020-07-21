Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

-----------------------------DFS-Recursion--------------------------------

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(x, y, board, word, i):
            if i == len(word):
                return True
            
            if y >= len(board) or x >= len(board[0]) or x < 0 or y < 0 or board[y][x] != word[i]:
                return False
            
            board[y][x] = 0   
            
            if search(x+1, y, board, word, i+1) or \
                  search(x-1, y, board, word, i+1) or \
                  search(x, y+1, board, word, i+1) or \
                  search(x, y-1, board, word, i+1) :
                return True
            
            board[y][x] = word[i]
            
            return False
    
        for y in range(len(board)):
            for x in range(len(board[0])):
                if search(x, y, board, word, 0):
                    return True
                    
        return False
