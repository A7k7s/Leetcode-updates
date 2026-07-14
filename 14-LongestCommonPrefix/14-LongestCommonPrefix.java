// Last updated: 7/14/2026, 2:06:15 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String r="";
        for(int i=0;i<strs[0].length();i++){
            char c=strs[0].charAt(i);
            for(int j=1;j<strs.length;j++){
                if(i>=strs[j].length() || strs[j].charAt(i)!=c){
                    return r;
                }
            }r=r+c;
        }return r;
    }
}