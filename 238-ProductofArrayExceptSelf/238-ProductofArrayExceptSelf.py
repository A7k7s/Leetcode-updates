# Last updated: 7/28/2026, 11:14:07 AM
1class Solution:
2    def productExceptSelf(self, nums):
3        n = len(nums)
4        output = [1] * n
5
6        left = 1
7        for i in range(n):
8            output[i] *= left
9            left *= nums[i]
10
11        right = 1
12        for i in range(n - 1, -1, -1):
13            output[i] *= right
14            right *= nums[i]
15
16        return output