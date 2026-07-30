# Last updated: 7/30/2026, 1:32:40 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        low = high = 0
4
5        for ch in s:
6            if ch == '(':
7                low += 1
8                high += 1
9            elif ch == ')':
10                low -= 1
11                high -= 1
12            else:  # '*'
13                low -= 1
14                high += 1
15
16            if high < 0:
17                return False
18
19            low = max(low, 0)
20
21        return low == 0