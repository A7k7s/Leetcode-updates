# Last updated: 7/14/2026, 2:05:02 PM
class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]