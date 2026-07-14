// Last updated: 7/14/2026, 2:01:20 PM
class Solution {
    public int maxDepth(String s) {
        int count=0;
        int mnum=0;
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(c=='('){
                count++;
                mnum=Math.max(mnum,count);
            }else if(c==')'){
                count--;
            }
        }return mnum;
    }
}