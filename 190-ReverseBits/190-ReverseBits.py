# Last updated: 7/14/2026, 2:04:05 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            res=(res<<1)|(n&1)
            n>>=1
        return res