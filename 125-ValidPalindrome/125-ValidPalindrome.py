# Last updated: 7/14/2026, 2:04:47 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        r=s[::-1]
        return r==s