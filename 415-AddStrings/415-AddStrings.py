# Last updated: 7/14/2026, 2:02:38 PM
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        return str(int(num1)+int(num2))