# Last updated: 7/14/2026, 2:05:12 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]

# Step 2: Merge and sort
        temp.extend(nums2)
        temp.sort()

# Step 3: Copy back into nums1 to modify it in-place
        for i in range(m + n):
            nums1[i] = temp[i] 

          
       
        