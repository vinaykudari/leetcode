# Dynamic Programming

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        bigL = len(word1)
        smalL = len(word2)
        if smalL > bigL:
            word1, word2 = word2, word1
            smalL, bigL = bigL, smalL
        
        prev_row = list(range(bigL+1))
        curr_row = [None]*(bigL+1)
        
        for i in range(1, smalL+1):
            curr_row[0] = i
            for j in range(1, bigL+1):
                if word2[i-1] != word1[j-1]:
                    curr_row[j] = min(prev_row[j], prev_row[j-1], curr_row[j-1]) + 1
                else:
                    curr_row[j] = prev_row[j-1]
            prev_row = curr_row
            curr_row = [None]*(bigL+1)
            
        return prev_row[bigL]
                
            
        
