# Hashmap

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.max_num = 0
        self.meta = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.meta:
            return False
        
        self.meta[val] = self.max_num
        self.data[self.max_num] = val
        self.max_num += 1
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.meta:
            return False
        
        del self.data[self.meta[val]]
        del self.meta[val]
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_num = random.randint(0, self.max_num-1)
        while random_num not in self.data:
            random_num = random.randint(0, self.max_num-1)
        return self.data[random_num]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
