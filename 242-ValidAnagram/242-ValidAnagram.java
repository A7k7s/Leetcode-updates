// Last updated: 7/14/2026, 2:03:38 PM
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        int []arr=new int[26];
        for(char ch:s.toCharArray()){
            arr[ch-'a']++;
        }
        for(char c:t.toCharArray()){
            if(arr[c-'a']==0){
                return false;
            }arr[c-'a']--;
        }return true;

    }
}