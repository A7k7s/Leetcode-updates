# Last updated: 8/22/2026, 10:19:27 AM
1from collections import deque
2
3class Solution:
4    def isCompleteTree(self, root: TreeNode) -> bool:
5        if not root:
6            return True
7        q = deque([root])
8        while q[0] is not None:
9            node = q.popleft()
10            q.append(node.left)
11            q.append(node.right)
12        while q and q[0] is None:
13            q.popleft()
14        return not bool(q)