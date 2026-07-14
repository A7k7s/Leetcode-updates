# Last updated: 7/14/2026, 2:06:21 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in strs[1:]:
                if i >= len(j) or j[i] != ch:
                    return r  
            r += ch  
        return r
