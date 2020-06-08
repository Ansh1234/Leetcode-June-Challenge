import numpy as np
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if(len(coins)==0):
            if(amount ==0 ):
                return 1
            else:
                return 0
        
        if(amount ==0):
            return 1
        
        matrix = np.zeros((len(coins), amount+1), dtype=int)
        
        for r_index, coin in enumerate(coins):
            row = matrix[r_index]
            for c_index, val in enumerate(row):
                if(c_index==0):
                    continue
                total = 0 
                if(r_index > 0):
                    total += matrix[r_index-1][c_index]
               
                c_index_temp = c_index - coin
                if(c_index_temp>=0):
                    total += matrix[r_index][c_index_temp]
                    
                if(c_index==coin):
                    total += 1
                row[c_index] = total
        
        
        return matrix[len(coins)-1][amount]
                    
        
