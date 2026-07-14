# Last updated: 7/14/2026, 2:02:29 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        m, n = len(g), len(s)
        g.sort()
        s.sort()
        count = 0 
        while i<m and j<n:
            if g[i]<=s[j]:
                count+=1
                j+=1
                i+=1
            else:
                j+=1
        return count

