# Last updated: 7/14/2026, 2:06:02 PM
class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        m={'(':')','[':']','{':'}'}
        for i in s:
            if i in m.keys():
                l.append(i)
            elif i in m.values():
                if l == [] or m[l.pop()] != i:
                    return False
            else:
                return False
        return len(l)==0

        