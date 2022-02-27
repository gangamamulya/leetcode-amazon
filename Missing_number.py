
class Solution(object):
    def missingNumber(self, nums):
        
        
        n = len(nums)+1 #3
        x = range(n+1)
        for i in range(0,n):
                if x[i] not in nums:
                    return x[i]
   
                
            
            
            
        
            
        
   
        
