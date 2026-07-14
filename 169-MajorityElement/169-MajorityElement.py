# Last updated: 7/14/2026, 2:04:15 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=floor(len(nums)/2)
        count=0
        candidate=None
        for i in nums:
            if count==0:
                candidate=i
            if i==candidate:
                count+=1
            else:
                count-=1
        return candidate