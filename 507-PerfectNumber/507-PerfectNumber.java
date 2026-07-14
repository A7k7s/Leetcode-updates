// Last updated: 7/14/2026, 2:02:17 PM
class Solution {
    public boolean checkPerfectNumber(int num) {
        int c=num/2;
        int count=0;
        for(int i=1;i<c+1;i++){
            if(num%i==0){
                count=count+i;
            }
        }return count==num;
    }
}