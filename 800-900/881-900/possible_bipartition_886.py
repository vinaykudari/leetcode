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
                
                
            
                
        
        
