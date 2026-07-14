# Last updated: 7/14/2026, 2:02:26 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc=0
        count=0
        for i in nums:
            if(i==1):
                count+=1
                maxc=max(count,maxc)
            else:
                count=0
        
        return maxc