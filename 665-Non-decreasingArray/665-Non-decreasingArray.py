# Last updated: 7/27/2026, 12:19:27 PM
1class Solution:
2    def checkPossibility(self, nums: List[int]) -> bool:
3        count = 0
4        for i in range(1, len(nums)):
5            if nums[i] < nums[i - 1]:
6                if count == 1:
7                    return False
8                count += 1
9                if i >= 2 and nums[i - 2] > nums[i]:
10                    nums[i] = nums[i - 1]
11                else:
12                    nums[i - 1] = nums[i]
13        return True