# Last updated: 7/28/2026, 11:14:25 AM
1class Solution:
2    def productExceptSelf(self, nums):
3        n = len(nums)
4        output = [1] * n
5        left = 1
6        for i in range(n):
7            output[i] *= left
8            left *= nums[i]
9        right = 1
10        for i in range(n - 1, -1, -1):
11            output[i] *= right
12            right *= nums[i]
13        return output