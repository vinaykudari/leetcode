Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

-----------------------------Hash-Map-----------------------------


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_frequency = {}
        
        for n in nums:
            number_frequency[n] = number_frequency.get(n, 0) + 1
                
        for num in number_frequency:
            if number_frequency[num] == 1:
                return num
            
        
