// Last updated: 7/14/2026, 2:01:59 PM
class Solution {
    public int pivotIndex(int[] nums) {
        int tsum=0;
       for(int i =0;i<nums.length;i++){
        tsum=tsum+nums[i];
        } 
        int p=-1;
        int lsum=0;
        for(int j=0;j<nums.length;j++){
         
            int rsum=tsum-lsum-nums[j];
            if(lsum==rsum){
                p=j;
                break;
            }
           lsum=lsum+nums[j];
        } 
        
      return p;
      }
}