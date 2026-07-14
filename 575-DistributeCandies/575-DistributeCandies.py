# Last updated: 7/14/2026, 2:02:07 PM
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        s=set(candyType)
        l=list(s)
        return min(n,len(l))
