# Sorting

import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1] 
        self.w = w
        
    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
                 


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
