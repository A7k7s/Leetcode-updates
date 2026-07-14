# Last updated: 7/14/2026, 2:04:34 PM
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        g=sum(gas)
        c=sum(cost)
        curr=0
        start=0
        if(g<c):
            return -1
        for i in range(0,len(gas)):
            curr+=gas[i]-cost[i]
            if curr<0:
                start=i+1
                curr=0
        return start

        