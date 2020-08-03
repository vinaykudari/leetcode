Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

------------------O(n)-----------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        N = len(s)-1
        i = 0
        
        while i < N:
            while not s[i].isalnum() and i < N:
                i += 1
            while not s[N].isalnum() and N > i:
                N -= 1
                
            if s[i] != s[N]:
                return False
            
            i += 1
            N -= 1
            
        return True
