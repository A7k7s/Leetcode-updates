# Last updated: 7/29/2026, 12:33:10 PM
1class Solution:
2    def findMaxLength(self, nums: List[int]) -> int:
3        prefix_sum = 0
4        first_occurrence = {0: -1}  
5        max_length = 0
6        for i, num in enumerate(nums):
7            if num == 1:
8                prefix_sum += 1
9            else:
10                prefix_sum -= 1
11            if prefix_sum in first_occurrence:
12                max_length = max(max_length, i - first_occurrence[prefix_sum])
13            else:
14                first_occurrence[prefix_sum] = i
15        return max_length