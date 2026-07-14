# Last updated: 7/14/2026, 2:05:37 PM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        for i in num1:
            n1=n1*10+(ord(i)-48)
        n2=0
        for i in num2:
            n2=n2*10+(ord(i)-48)
        return(str(n1*n2))