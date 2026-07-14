// Last updated: 7/14/2026, 2:05:35 PM
class Solution {
    public int jump(int[] nums) {
        if (nums.length <= 1) return 0;  
        int jumps = 0;          
        int maxReach = 0;      
        int currentEnd = 0;     
        for (int i = 0; i < nums.length - 1; i++) {
            maxReach = Math.max(maxReach, i + nums[i]);
             if (i == currentEnd) {
                jumps++;
                currentEnd = maxReach;
                if (i >= maxReach) {
                    return -1;
                }
            }
        }
        return jumps;
    }
}