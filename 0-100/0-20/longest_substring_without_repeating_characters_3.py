Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

--------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        mp = {}
        ans = 0
        st_idx = 0

        for idx, ch in enumerate(s):
            if ch in mp:
                st_idx = max(mp[ch]+1, st_idx)

            ans = max(ans, idx - st_idx + 1)
            mp[ch] = idx

        return ans



