Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

-------------------------Math------------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_bin(n1, n2, c):
            return (n1 + n2 + c)%2, (n1+n2+c)//2
            
        a_len, b_len = len(a), len(b)
        res = []
        carry = 0
        
        if a_len - b_len > 0:
            b = '0'*(a_len-b_len) + b
        else:
            a = '0'*(b_len-a_len) + a

        for _ in range(max(a_len, b_len)-1, -1, -1):
            sum, carry = add_bin(int(a[_]), int(b[_]), carry)
            res.append(str(sum))
            
        if carry:
            return '1' + ''.join(res[::-1])
        
        return ''.join(res[::-1])
