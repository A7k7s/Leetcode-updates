// Last updated: 7/14/2026, 2:04:01 PM
class Solution {
    public boolean isHappy(int n) {
        while (n != 1 && n != 4) {   
            int count = 0;           
            while (n > 0) {         
                count = count + (n % 10) * (n % 10);
                n = n / 10;
            }
            n = count;               
        }
        return n == 1;
    }
}
