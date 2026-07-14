// Last updated: 7/14/2026, 2:01:30 PM
class Solution {
    public int minCostToMoveChips(int[] position) {
        int odd=0;
        int even=0;
        for(int i:position){
            if(i%2==0){
                even++;
            }else{
                odd++;
            }
        }return Math.min(odd,even);
    }
}