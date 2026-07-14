# Last updated: 7/14/2026, 2:04:30 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        r=' '.join(reversed(words))
        return r
        