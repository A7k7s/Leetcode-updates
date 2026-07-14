// Last updated: 7/14/2026, 2:05:51 PM
class Solution {
    public int strStr(String haystack, String needle) {
        int i=0;
        if(haystack.contains(needle)){
            i=haystack.indexOf(needle);
        }
        else{
            i=-1;
        }
        return i;
    }
}