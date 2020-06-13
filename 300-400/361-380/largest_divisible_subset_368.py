# Dynamic Programming

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        nums.sort()
        N = len(nums)
        
        dp = [1] * N
        prev = [-1] * N
        
        maxIndex = 0
        res = []
        
        for i in range(1, N): 
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[maxIndex]:
                maxIndex = i
                
        while maxIndex > -1:
            res.append(nums[maxIndex])
            maxIndex = prev[maxIndex]
            
        return res
