# Recursion

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, l, i=0):
            if i == l//2:
                return
            reverse(s, l, i+1)
            s[i], s[l-i-1] = s[l-i-1], s[i]
            
        reverse(s, len(s))
        
