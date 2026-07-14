# Last updated: 7/14/2026, 2:00:34 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l=[]
        while(n!=0):
            t=n%10
            if t!=0:
                l.append(t)
            n=n//10
        l=l[::-1]
        r=sum(l)
        res=0
        for i in l:
            res=res*10+i
        return res*r