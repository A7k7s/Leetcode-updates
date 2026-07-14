# Last updated: 7/14/2026, 2:01:56 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winsum=sum(nums[:k])
        max_sum=winsum
        for i in range(k,len(nums)):
            winsum=winsum-nums[i-k]+nums[i]
            max_sum=max(max_sum,winsum)
        return max_sum/k