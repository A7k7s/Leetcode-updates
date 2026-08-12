# Last updated: 8/12/2026, 12:29:06 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels = {'a', 'e', 'i', 'o', 'u'}
4        count = 0
5        for i in range(k):
6            if s[i] in vowels:
7                count += 1
8        ans = count
9        for i in range(k, len(s)):
10            if s[i] in vowels:
11                count += 1
12            if s[i - k] in vowels:
13                count -= 1
14            ans = max(ans, count)
15            if ans == k:
16                return k
17        return ans