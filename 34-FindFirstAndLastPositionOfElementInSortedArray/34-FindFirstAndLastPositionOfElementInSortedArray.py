# Last updated: 7/14/2026, 2:05:45 PM
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                l.append(i)
        n=[]
        if len(l)==0:
            n.append(-1)
            n.append(-1)
        else:
            n.append(l[0])
            n.append(l[-1])
        return n

        