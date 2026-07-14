// Last updated: 7/14/2026, 2:04:20 PM
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;
        
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;  
            }
            count += (num == candidate) ? 1 : -1; 
        }
        
        return candidate;
    }
}
