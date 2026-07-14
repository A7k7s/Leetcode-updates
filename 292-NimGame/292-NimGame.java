// Last updated: 7/14/2026, 2:03:13 PM
class Solution {
    public boolean canWinNim(int n) {
        
        if(n<=3){
            return true;
        }else{
            if(n%4==0){
                return false;
            }else{
                return true;
            }
        }
        
    }
}