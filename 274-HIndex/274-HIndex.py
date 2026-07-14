# Last updated: 7/14/2026, 2:03:19 PM
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations=sorted(citations)
        for i in range(0,len(citations)):
            if(citations[i]>=len(citations)-i):
                return len(citations)-i
        return 0
        