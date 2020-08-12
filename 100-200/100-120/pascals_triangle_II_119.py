Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

---------------------------------------------------

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate_pascal(rowIndex):
            def helper(row, n):
                newRow = [1]
                for i in range(1, n):
                    newRow.append(row[i]+row[i-1])
                newRow.append(1)
                return newRow
            
            triangle = [ [1],
                        [1,1]
                       ]
            
            if rowIndex < 1:
                return triangle[rowIndex]
            
            for i in range(2, rowIndex+1):
                triangle.append(helper(triangle[-1], i))
                
            return triangle[-1]
                
        return generate_pascal(rowIndex)
