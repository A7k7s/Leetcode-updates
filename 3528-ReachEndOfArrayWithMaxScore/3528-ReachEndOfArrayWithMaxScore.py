# Last updated: 7/14/2026, 2:00:39 PM
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        result = maxele = 0
        for i in nums:
            result += maxele
            maxele = max(maxele, i)
        return result
            
