// Last updated: 7/14/2026, 2:00:52 PM
class Solution {
    public int averageValue(int[] nums) {
        int sum=0;
        int count=0;
        for (int i:nums){
            if(i%2==0 && i%3==0){
                sum+=i;
                count++;
            }

        }
        if(count==0){
            return sum;
        }else{
            return sum/count;
        }
    }
}