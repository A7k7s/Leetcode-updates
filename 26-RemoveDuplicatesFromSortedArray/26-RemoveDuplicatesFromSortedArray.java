// Last updated: 7/14/2026, 2:06:01 PM
class Solution {
    public int removeDuplicates(int[] nums) {
         int n = nums.length;
        
        if (n == 0) return 0;  

        Arrays.sort(nums);  
        int uniqueIndex = 1;  
        
        for (int i = 1; i < n; i++) {
           
            if (nums[i] != nums[i - 1]) {
                nums[uniqueIndex] = nums[i]; 
                uniqueIndex++ ; 
            }
        }

        return uniqueIndex;  
    
    }
}