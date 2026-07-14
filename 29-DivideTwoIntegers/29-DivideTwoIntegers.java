// Last updated: 7/14/2026, 2:05:48 PM
class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;  // Return the maximum value of a 32-bit signed integer
        }
        int y= dividend/divisor;
        return y;
    }
}