Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

-------------------------Hash-Map-------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            if target-num in hash_map:
                return [index, hash_map[target-num]]
            hash_map[num] = index
