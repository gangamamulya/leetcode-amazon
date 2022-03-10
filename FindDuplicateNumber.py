class Solution(object):
    def findDuplicate(self, nums):
        alreadyseen = set()
        for item in nums:
            if item in alreadyseen:
                return item
            else:
                alreadyseen.add(item)
                
