# Last updated: 8/11/2026, 12:28:30 PM
1class Solution(object):
2    def calculate(self, s):
3        total = 0
4        last = 0
5        num = 0
6        op = "+"
7        for i in range(len(s)):
8            if s[i].isdigit():
9                num = num * 10 + int(s[i])
10            if s[i] in "+-*/" or i == len(s) - 1:
11                if op == "+":
12                    total += last
13                    last = num
14                elif op == "-":
15                    total += last
16                    last = -num
17                elif op == "*":
18                    last = last * num
19                elif op == "/":
20                    if last < 0:
21                        last = -(-last // num)
22                    else:
23                        last = last // num
24                op = s[i]
25                num = 0
26        return total + last