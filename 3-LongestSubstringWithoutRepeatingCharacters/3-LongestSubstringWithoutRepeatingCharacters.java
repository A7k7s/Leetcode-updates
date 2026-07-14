// Last updated: 7/14/2026, 2:06:28 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int []freq=new int[128];
        int left=0;
        int mlen=0;
        for(int right=0;right<s.length();right++){
            char ch=s.charAt(right);
            freq[ch]++;
            while(freq[ch]>1){
                freq[s.charAt(left)]--;
                left++;
            }
            mlen=Math.max(mlen,right-left+1);
        }return mlen;
    }
}