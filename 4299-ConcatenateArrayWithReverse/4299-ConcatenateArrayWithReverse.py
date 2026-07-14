# Last updated: 7/14/2026, 2:00:36 PM
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        size=len(nums)-1
        for j in range(len(nums)):
            nums.append(nums[size-j])
        return nums