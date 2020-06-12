class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) -1
        
        while(start <= end):
            
            if(start == end):
                if(target<=nums[start]):
                    return start
                else:
                    return start + 1
            
            if(end-start ==1):
                if(target <= nums[start]):
                    return start
                elif(target <= nums[end]):
                    return end
                else:
                    return end+1
            
            mid = int((start + end + 1) / 2)
            if(target == nums[mid]):
                return mid
            elif(target<nums[mid]):
                end = mid-1
            else:
                start = mid+1
            
            
            
        return len(nums)
            
