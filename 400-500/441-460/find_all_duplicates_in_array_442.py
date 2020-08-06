
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

---------------------------O(n)----------------------------

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        for i in range(N):
            index = (nums[i]-1)%N 
            nums[(nums[i]-1)%N] += N
            if nums[(nums[i]-1)%N] > 2*N:
                res.append((nums[i]-1)%N+1)
        
        return res
