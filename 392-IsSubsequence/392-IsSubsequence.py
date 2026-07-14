# Last updated: 7/14/2026, 2:02:48 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        o = False
        for i in s:
            if i in t:
                index = t.index(i)
                t = t[index + 1:]
                o = True
            else:
                return False
        return o