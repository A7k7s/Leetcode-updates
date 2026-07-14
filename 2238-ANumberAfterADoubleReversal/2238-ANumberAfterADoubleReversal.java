// Last updated: 7/14/2026, 2:01:03 PM
class Solution {
    public boolean isSameAfterReversals(int num) {
        int fin=num;
        int rev1=0;
        int rev2=0;
        while(num>0){
            rev1=rev1*10+(num%10);
            num/=10;
        }
        while(rev1>0){
            rev2=rev2*10+(rev1%10);
            rev1/=10;
        }
    return rev2==fin;


    }
}