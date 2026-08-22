# Last updated: 8/22/2026, 11:31:10 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        if not root:
17            return ""
18        result=[]
19        def preorder(node):
20            if not node:
21                return
22            result.append(str(node.val))
23            preorder(node.left)
24            preorder(node.right)
25        preorder(root)
26        return ",".join(result)
27
28    def deserialize(self, data):
29        """Decodes your encoded data to tree.
30        
31        :type data: str
32        :rtype: TreeNode
33        """
34        if not data:
35            return None
36        values=list(map(int,data.split(",")))
37        def build(left, right):
38            if left > right:
39                return None
40            root = TreeNode(values[left])
41            index = left + 1
42            while index <= right and values[index] < root.val:
43                index += 1
44            root.left = build(left + 1, index - 1)
45            root.right = build(index, right)
46            return root
47        return build(0, len(values) - 1)
48        
49
50# Your Codec object will be instantiated and called as such:
51# ser = Codec()
52# deser = Codec()
53# tree = ser.serialize(root)
54# ans = deser.deserialize(tree)
55# return ans