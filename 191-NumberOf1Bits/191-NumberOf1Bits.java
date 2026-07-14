// Last updated: 7/14/2026, 2:04:03 PM
class Solution {
    public int hammingWeight(int n) {
        int count=0;
        while(n!=0){
            if(n%2==1){
                count++;
            }
            n=n/2;
        }
        return count;
    }
}