# Last updated: 7/14/2026, 2:05:44 PM
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        nums.sort()
        i=nums.index(target)
        return i
        