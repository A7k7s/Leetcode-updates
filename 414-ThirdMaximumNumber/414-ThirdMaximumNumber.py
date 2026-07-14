# Last updated: 7/14/2026, 2:02:40 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=set(nums)
        num=list(n)
        num.sort(reverse=True)
        if len(num)<3:
            return max(n)
        else:
            return num[2]