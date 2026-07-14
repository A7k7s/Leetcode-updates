// Last updated: 7/14/2026, 2:06:19 PM
class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int t=x;
        int ans=0;
        while(x>0){
			int n=x%10;
			ans=ans*10+n;
			x=x/10;
		}
        return t==ans;
    }
}