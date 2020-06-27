Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

------------------Dynamic-Programming---------------

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0], dp[1] = 0, 1
        
        for i in range(2, n+1):
            for j in range(1, floor(sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
