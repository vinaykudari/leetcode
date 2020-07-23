Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

--------------------Bit-manipulation---------------------

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
#         nums_set = set(nums)
#         n = sum(nums)
#         m = sum(nums_set)
#         x = 2*m - n
        
#         for n in nums_set:
#             if x-n in nums_set:
#                 return [n, x-n]

        res = reduce(xor, nums)
        b = (res & (res-1)) ^ res
        n1 = reduce(xor, filter(lambda n: n & b, nums))
        
        return [n1, res^n1]
