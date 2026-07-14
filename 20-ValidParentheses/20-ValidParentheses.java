// Last updated: 7/14/2026, 2:06:07 PM
class Solution {
    public boolean isValid(String s) {
        Stack<Character> st=new Stack<>();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='{'){
                st.push('}');
            }else if(s.charAt(i)=='('){
                st.push(')');
            }else if(s.charAt(i)=='['){
                st.push(']');
            }else if(st.isEmpty()||s.charAt(i)!=st.pop()){
                return false;
            }
        }return st.isEmpty();
    }
}