Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

------------------------------Heap-------------------------------

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        num_freq = Counter(nums).items()
        
        heap = []
        res = []
        
        for num in num_freq:
            k -= 1
            heapq.heappush(heap, (-num[1], num[0]))
            if k < 0:
                heapq.heappop(heap)
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res
