class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)  
        for i in range(0,n): 
            for j in range(i+1,n): 
                if(target == nums[i] + nums[j]): 
                    return i,j
