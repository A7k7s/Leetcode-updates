// Last updated: 7/14/2026, 2:02:34 PM
class Solution {
    public int arrangeCoins(int n) {
        int i=1;
        while(n>0){
            i++;
            n=n-i;
        }return i-1;
    }
}