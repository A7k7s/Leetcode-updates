// Last updated: 7/14/2026, 2:04:41 PM
class Solution {
    public boolean isPalindrome(String s) {
        if(s.length()==0){
            return false;
        }String r=s.replaceAll("[^A-Za-z0-9]","");
        r=r.toLowerCase();
        int left=0,right=r.length()-1;
        while(left<right){
            if(r.charAt(left)!=r.charAt(right)){
                return false;
            }left++;
            right--;
        }return true;
    }
}