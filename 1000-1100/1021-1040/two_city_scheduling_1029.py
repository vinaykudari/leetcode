# Heap

import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # heap O(N*log(N))
        heap, n, cost = [], len(costs), 0
        
        # O(N)
        for _ in range(n):
            heapq.heappush(heap, (costs[_][1]-costs[_][0], _))
        
        # O(N/2*log(N))
        for _ in range(n//2):
            cost += costs[heapq.heappop(heap)[1]][1]

        for _, index in heap:
            cost += costs[index][0]
                           
        return cost
    
        # sorting O(N*logN)
        
        # costs.sort(key=lambda x : x[0]-x[1])
        # cost, n = 0, len(costs)
        # for i in range(n):
        #     if i+1 <= n/2:
        #         cost += costs[i][0]
        #     else:
        #         cost += costs[i][1]
        # return cost
        
