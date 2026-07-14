// Last updated: 7/14/2026, 2:03:17 PM
class Solution {
    public int findDuplicate(int[] nums) {
        int r=0;
        HashMap<Integer,Integer>hs=new HashMap<>();
        for(int i:nums){
            hs.put(i,hs.getOrDefault(i,0)+1);
        }
        for(Map.Entry<Integer,Integer>e:hs.entrySet()){
            if(e.getValue()>1) r=e.getKey();
        }
        return r;
    }
}