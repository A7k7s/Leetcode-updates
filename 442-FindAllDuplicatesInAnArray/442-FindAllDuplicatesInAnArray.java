// Last updated: 7/14/2026, 2:02:35 PM
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer>l=new ArrayList<>();
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]==nums[i+1]) l.add(nums[i+1]);
        }return l;
    }
}