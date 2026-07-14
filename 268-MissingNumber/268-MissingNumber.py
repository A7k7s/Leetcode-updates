# Last updated: 7/14/2026, 2:03:22 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=sum(nums)
        s=0
        for i in range(len(nums)+1):
            s+=i
        return s-n
        