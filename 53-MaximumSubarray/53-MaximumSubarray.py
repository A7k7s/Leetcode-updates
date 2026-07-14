# Last updated: 7/14/2026, 2:05:31 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        current_sum=nums[0]
        for i in nums[1:]:
            current_sum=max(i,current_sum+i)
            max_sum=max(max_sum,current_sum)
        return max_sum

        