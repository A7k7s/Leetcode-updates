# Last updated: 8/11/2026, 11:34:17 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def tree2str(self, root):
9        if root is None:
10            return ""
11        ans = str(root.val)
12        if root.left:
13            ans += "(" + self.tree2str(root.left) + ")"
14        if root.right:
15            if root.left is None:
16                ans += "()"
17            ans += "(" + self.tree2str(root.right) + ")"
18        return ans
19        