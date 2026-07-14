# Last updated: 7/14/2026, 2:02:54 PM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,'',1)
            else:
                return False
        return True
        