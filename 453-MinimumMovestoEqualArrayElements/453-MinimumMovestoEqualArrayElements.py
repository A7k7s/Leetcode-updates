# Last updated: 7/29/2026, 12:37:12 PM
1class Solution:
2    def minMoves(self, nums: List[int]) -> int:
3        s=0
4        nums=sorted(nums)
5        t=nums[0]
6        for i in range(1,len(nums)):
7            s+=nums[i]-t
8        return s