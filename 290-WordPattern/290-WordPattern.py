# Last updated: 7/14/2026, 2:03:15 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))