# Last updated: 7/14/2026, 2:05:15 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        list=[0]*(n+1)
        list[0]=1
        list[1]=1
        if n==0 or n==1:
            return 1
        else:
            for i in range(2,n+1):
                list[i]=list[i-1]+list[i-2]
            return list[n]
        