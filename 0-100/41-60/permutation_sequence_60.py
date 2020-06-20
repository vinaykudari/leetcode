The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

# Math

import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        res = ''
        fact = {
            0:1,
            1:1
        }
        
        def get_fact(n):
            if n in fact:
                return fact[n]
            for i in range(2, n+1):
                fact[i] = i * fact[i-1]
                    
        get_fact(n-1)
        
        while k > 1: 
            res += str(nums[math.ceil(k / fact[n-1])-1])
            nums.remove(nums[math.ceil(k / fact[n-1])-1])
            k %= fact[n-1]
            if k == 0:
                res += ''.join(str(n) for n in nums[::-1])
                return res
            n -= 1
        
        res += ''.join(str(n) for n in nums)    
        return res
