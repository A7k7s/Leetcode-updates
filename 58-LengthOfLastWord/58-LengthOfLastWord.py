# Last updated: 7/14/2026, 2:05:24 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()[-1]
        return len(l)
        