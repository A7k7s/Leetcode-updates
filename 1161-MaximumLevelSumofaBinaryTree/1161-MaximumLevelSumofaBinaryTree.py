# Last updated: 8/22/2026, 10:20:42 AM
1from collections import deque
2
3class Solution:
4    def maxLevelSum(self, root):
5        if not root:
6            return 0
7
8        queue = deque([root])
9        max_sum = float('-inf')
10        max_level = 1
11        current_level = 1
12
13        while queue:
14            level_size = len(queue)
15            level_sum = 0
16
17            for _ in range(level_size):
18                node = queue.popleft()
19                level_sum += node.val
20
21                if node.left:
22                    queue.append(node.left)
23                if node.right:
24                    queue.append(node.right)
25
26            if level_sum > max_sum:
27                max_sum = level_sum
28                max_level = current_level
29
30            current_level += 1
31
32        return max_level