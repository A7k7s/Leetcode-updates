// Last updated: 7/14/2026, 2:01:37 PM
class Solution {
    public String removeOuterParentheses(String s) {
        String r="";
        int count=0;
        for(int i=0;i<s.length()-1;i++){
            if(s.charAt(i)==')') count--;
            if(count!=0){
                r=r+s.charAt(i);
            }
            if(s.charAt(i)=='(') count++;
        }return r;
    }
}