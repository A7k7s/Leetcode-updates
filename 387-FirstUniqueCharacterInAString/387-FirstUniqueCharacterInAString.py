# Last updated: 7/14/2026, 2:02:59 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1

        