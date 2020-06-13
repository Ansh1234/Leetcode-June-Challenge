class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        d = {}
        final_max_set = []
        nums = sorted(nums)
        
        for index, num in enumerate(nums):
            
            i = 0
            max_set = set()
            while(i < index):
                if num%nums[i]==0:
                    if(len(d[i])> len(max_set)):
                        max_set = set(d[i])
                i+=1
            
            max_set.add(num)
            d[index] = max_set
            if(len(max_set) > len(final_max_set)):
                final_max_set = max_set
                     
        return final_max_set
