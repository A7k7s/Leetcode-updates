// Last updated: 7/14/2026, 2:05:05 PM
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int r=0;
        for(int j=m;j<n+m;j++){
            nums1[j]=nums2[r];
            r++;
        }
        Arrays.sort(nums1);
        
        
    }
}