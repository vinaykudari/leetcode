# Sets

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        
        set1, set2 = set(), set()
        de = collections.deque(dislikes)
        x, y = de.popleft()
        l = len(dislikes)
        
        set1.add(x)
        set2.add(y)
        
        i = 0
        
        while len(de) != 1:
            x, y = de.popleft()
            if x in set1:
                if y in set1: return False
                set2.add(y)
            elif x in set2:
                if y in set2: return False
                set1.add(y)   
            elif y in set1:
                set2.add(x)
            elif y in set2:
                set1.add(x)
            else:
                if i == l:
                    set1.add(x)
                    set2.add(y)
                else:
                    de.append([x, y])
                
            i += 1
            
        x, y = de.popleft()  
        if (x in set1 and y in set1) or (x in set2 and y in set2):
            return False
        else:
            return True
                
                
# Graph - BFS - Two Color

from collections import deque
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        
        def get_adjacency_list(dislikes, N):
            adjacency_list = defaultdict(list)
            for dislike in dislikes:
                adjacency_list[dislike[0]-1].append(dislike[1]-1)
                adjacency_list[dislike[1]-1].append(dislike[0]-1)
            return adjacency_list
        
        def bfs_is_bipartite(adjacency_list, N):
            visited = [False] * N
            color = [-1] * N
            
            for i in range(N):
                queue = deque([i])
                visited[i] = True

                while queue:
                    u = queue.pop()
                    if color[u] == -1:
                        color[u] = True
                    for v in adjacency_list[u]:
                        if color[u] == color[v]:
                            return False
                        if not visited[v]:
                            queue.append(v)
                            visited[v] = True
                            color[v] = not color[u]

            return True
            
        
        adjacency_list = get_adjacency_list(dislikes, N)
        return bfs_is_bipartite(adjacency_list, N)            
                
        
        
