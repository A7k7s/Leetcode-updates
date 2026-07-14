# Last updated: 7/14/2026, 2:05:40 PM
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        # Step 1: Place numbers in their correct positions
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # Step 2: Identify the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
