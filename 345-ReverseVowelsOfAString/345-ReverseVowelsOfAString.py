# Last updated: 7/14/2026, 2:03:02 PM
class Solution:
    def rev(self,s,left,right):
        l=['a','e','i','o','u','A','E','I','O','U']
        if left >= right:
            return s
        if(s[left] not in l):
            return self.rev(s,left+1,right)
        elif(s[right] not in l):
            return self.rev(s,left,right-1)
        else:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            return self.rev(s,left+1,right-1)
    def reverseVowels(self, s: str) -> str:
        out = list(s)
        out = self.rev(out, 0, len(out) - 1)
        return ''.join(out)