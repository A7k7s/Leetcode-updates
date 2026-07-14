# Last updated: 7/14/2026, 2:06:27 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ma=nums1+nums2
        ma.sort()
        i=len(ma)
        if i%2==0:
            r=(ma[i//2]+ma[(i//2)-1])/2.0
        else:
            r=ma[i//2]
        return float(r)