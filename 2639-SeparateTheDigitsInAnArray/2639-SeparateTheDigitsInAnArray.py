# Last updated: 7/14/2026, 2:00:45 PM
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            for c in str(i):
                ans.append(int(c))
        return ans
