# Last updated: 7/14/2026, 2:03:32 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ss=sorted(s)
        ts=sorted(t)
        for i,j in zip(ss,ts):
            if i!=j:
                return False
        return True
            
        