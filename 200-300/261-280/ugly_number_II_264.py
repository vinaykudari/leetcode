Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

----------------------Heap----------------------

class Temp:
    def __init__(self):
        self.heap = []
        self.res = []
        self.stack = {1, }
        heapq.heappush(self.heap, 1)
        
        for _ in range(1690):
            temp = heapq.heappop(self.heap)
            for multiple in [2, 3, 5]:
                val = temp*multiple
                if val not in self.stack:
                    heapq.heappush(self.heap, val)
                    self.stack.add(val)
                    
            self.res.append(temp)
    
class Solution:
    obj = Temp()
    def nthUglyNumber(self, n: int) -> int:
        return self.obj.res[n-1]
