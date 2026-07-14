# Last updated: 7/14/2026, 2:04:11 PM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)
        return ans