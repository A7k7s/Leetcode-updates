# Last updated: 7/14/2026, 2:04:36 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
           return 0
        k = sorted(set(nums))
        longest = 1
        current = 1
        for i in range(1, len(k)):
            if k[i] == k[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current
                )
                current = 1
        longest = max(longest, current)
        return longest