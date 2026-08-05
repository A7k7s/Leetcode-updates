# Last updated: 8/5/2026, 10:57:25 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left, right = 0, len(numbers) - 1
4        while left < right:
5            curr_sum = numbers[left] + numbers[right]
6            if curr_sum == target:
7                return [left + 1, right + 1]  
8            elif curr_sum < target:
9                left += 1
10            else:
11                right -= 1
12