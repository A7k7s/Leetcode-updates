# Last updated: 7/14/2026, 2:02:58 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=list(set(nums1)&set(nums2))
        
        return r