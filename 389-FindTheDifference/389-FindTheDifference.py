# Last updated: 7/14/2026, 2:02:49 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss=sorted(s)
        ts=sorted(t)
        for i,j in zip(ss,ts):
            if i!=j:
                return j
        return ts[-1]
        