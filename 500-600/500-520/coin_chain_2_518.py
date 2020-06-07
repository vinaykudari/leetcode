class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in coins:
            for j in range(i, amount+1):
                dp[j] += dp[j-i]
        return dp[amount]
        
        
#         grid = [[0 for i in range(amount+1)] for _ in range(len(coins)+1)]
        
#         for i in range(len(grid)):
#             grid[i][0] = 1
                
        
#         for i in range(1, len(grid)):
#             for j in range(1, amount+1):
#                 if coins[i-1] <= j:
#                     grid[i][j] = grid[i-1][j] + grid[i][j - coins[i-1]]
#                 else:
#                     grid[i][j] = grid[i-1][j]
                    
#         return grid[-1][-1]
