import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values_to_indexes = {}
        self.indexes_to_values = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values_to_indexes:
            return False
        else:
            length = len(self.values_to_indexes)
            self.values_to_indexes[val] = length +1
            self.indexes_to_values[length+1] = val       
            return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.values_to_indexes:
            return False
        else:
            index = self.values_to_indexes[val]
            if(index == len(self.values_to_indexes)):
                del self.values_to_indexes[val]
                del self.indexes_to_values[index]
            else:
                last_index_val = self.indexes_to_values[len(self.values_to_indexes)]
                
                del self.values_to_indexes[val]
                self.values_to_indexes[last_index_val] = index
                
                del self.indexes_to_values[len(self.indexes_to_values)]
                self.indexes_to_values[index] = last_index_val
            
            return True
                
                
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if(len(self.values_to_indexes)==0):
            return None
        index = random.randint(1, len(self.values_to_indexes))
        return self.indexes_to_values[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
