// Last updated: 7/14/2026, 2:00:48 PM
class Solution {
    public int maximumCount(int[] nums) {
        int p=0;
        int n=0;
        for (int i:nums){
            if(i>0){
                p++;
            }else if(i<0){
                n++;
            }
        }
        if(p>n){
            return p;
        }return n;
    }
}