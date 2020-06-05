import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.indexes = list(range(len(self.w)))
        self.weights = list()
        self.s = 0
        

    def pickIndex(self) -> int:
        if(self.s==0):
            self.weights = list(self.w)
            self.s = sum(self.weights)
        
        index = random.choices(self.indexes, self.weights)[0]
        self.weights[index] -= 1
        self.s -= 1 
        
        return index
        
        
          
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
