// Last updated: 7/14/2026, 2:01:48 PM
class Solution {
    public boolean rotateString(String s, String goal) {
        if(s.length()!=goal.length()) return false;
        return (s+s).contains(goal);
        
    }
}