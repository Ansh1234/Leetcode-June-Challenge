class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if(n<1):
            return False
        
        while(n>1):
            if(n%2 !=0):
                return False
            n = int(n/2)
            
        if(n==1):
            return True
            
