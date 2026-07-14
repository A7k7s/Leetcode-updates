# Last updated: 7/14/2026, 2:00:41 PM
class Solution:
    def finalString(self, s: str) -> str:
        res=""
        for i in s:
            if i=="i":
                res=res[::-1]
            else:
                res=res+i
        return res