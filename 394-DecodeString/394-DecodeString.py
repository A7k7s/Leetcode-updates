# Last updated: 8/13/2026, 1:37:56 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack = []
4        for char in s:
5            if char != "]":
6                stack.append(char)
7            else: 
8                curr_str = ""
9                while stack[-1] != "[":
10                    curr_str = stack.pop() + curr_str
11                stack.pop()
12                curr_num = ""
13                while stack and stack[-1].isdigit():
14                    curr_num = stack.pop() + curr_num
15                curr_str = int(curr_num) * curr_str
16                stack.append(curr_str)
17        return "".join(stack)
18