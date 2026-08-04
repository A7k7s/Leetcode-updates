# Last updated: 8/4/2026, 12:35:38 PM
1class Solution:
2    def minFlipsMonoIncr(self, s):
3        rightZeros = s.count('0')
4        leftOnes = 0
5        ans = rightZeros
6        for ch in s:
7            if ch == '0':
8                rightZeros -= 1
9            else:
10                leftOnes += 1
11            ans = min(ans, leftOnes + rightZeros)
12        return ans