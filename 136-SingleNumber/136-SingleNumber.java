// Last updated: 7/14/2026, 2:04:31 PM
class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int r=0;
        for(int i:nums){
            r=r^i;
        }
        return r;
    }
}