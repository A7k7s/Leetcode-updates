# Last updated: 7/14/2026, 2:00:30 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)
        out=abs(nums[0]-nums[n-1])
        for i in range(n-1):
            out=max(out,abs(nums[i]-nums[i+1]))
        return out