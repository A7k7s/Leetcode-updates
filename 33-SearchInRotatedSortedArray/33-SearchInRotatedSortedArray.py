# Last updated: 7/14/2026, 2:05:47 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i==target:
                return nums.index(i)
        return -1