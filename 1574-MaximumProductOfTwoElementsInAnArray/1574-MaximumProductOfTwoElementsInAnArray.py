# Last updated: 7/14/2026, 2:01:22 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        res=(nums[-1]-1)*(nums[-2]-1)
        return res
        