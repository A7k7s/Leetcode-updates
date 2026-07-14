# Last updated: 7/14/2026, 2:01:55 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls=0
        ts=sum(nums)
        for i in range(len(nums)):
            rs=ts-ls-nums[i]
            if(ls==rs):
                return i
            else:
                ls+=nums[i]
        return -1
    
        