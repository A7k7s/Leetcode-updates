# Last updated: 7/14/2026, 2:01:09 PM
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre=0
        post=0
        for i in range(len(nums)):
            if(i==0):
                pre=0
                post=sum(nums[1:])
            elif (i==len(nums)-1):
                pre=sum(nums[:i])
                post=0
            else:
                pre=sum(nums[:i])
                post=sum(nums[i+1:])
            if(pre==post):
                return i
        return -1 
        