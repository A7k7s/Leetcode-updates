// Last updated: 7/14/2026, 2:06:22 PM
class Solution {
    public int reverse(int x) {
        long rev1=0;
        while(x!=0){
            rev1=rev1*10+(x%10);
            x/=10;
        }
        if (rev1 > Integer.MAX_VALUE  || (rev1 < Integer.MIN_VALUE )) {
                return 0;  
        }else{
            return (int)rev1;
        }
    }
}