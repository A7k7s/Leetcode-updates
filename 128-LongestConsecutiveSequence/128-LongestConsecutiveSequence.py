# Last updated: 8/24/2026, 4:04:12 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if not nums:
4           return 0
5        k = sorted(set(nums))
6        longest = 1
7        current = 1
8        for i in range(1, len(k)):
9            if k[i] == k[i - 1] + 1:
10                current += 1
11            else:
12                longest = max(longest, current
13                )
14                current = 1
15        longest = max(longest, current)
16        return longest