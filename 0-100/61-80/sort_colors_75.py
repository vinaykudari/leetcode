class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        low, mid, high = 0, 0, len(nums)-1
        
        while mid <= high:
            if nums[mid] == 2:
                swap(mid, high)
                high -= 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(mid, low)
                low += 1
                mid += 1
