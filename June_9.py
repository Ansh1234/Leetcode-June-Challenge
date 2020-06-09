class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if(s == "" and t == ""):
            return True
        elif(s == ""):
            return True
        elif(t == ""):
            return False
         
        if(len(s)>len(t)):
            return False
        
        s_index = 0
        t_index = 0
        
        while(True):
            
            if(s_index == len(s)):
                break
            
            if(t_index >= len(t)):
                return False
            
            
            if(s[s_index] == t[t_index]):
                s_index +=1 
                t_index +=1
            else:
                t_index+=1
                
        return True
            
        
        
