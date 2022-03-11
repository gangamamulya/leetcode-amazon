class LargerNumKey(str):
    def __lt__(x, y):  
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        op_str = map(str, nums)  #convert to string
        sort_array=sorted(op_str, key=LargerNumKey) # sort the array which has strings in it
        largest_num = ''.join(sort_array)
        if largest_num[0] == '0' :
            return '0'
        else:
            return largest_num
