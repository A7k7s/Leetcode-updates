# Last updated: 7/14/2026, 2:02:15 PM
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (
            word.isupper() or 
            word.islower() or   
            (word[0].isupper() and word[1:].islower())
        )