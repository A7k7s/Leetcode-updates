# Last updated: 7/14/2026, 2:03:52 PM
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=sorted(nums)
        return n[len(n)-k]
        