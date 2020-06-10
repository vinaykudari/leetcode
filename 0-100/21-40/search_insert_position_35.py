# Binary Search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
