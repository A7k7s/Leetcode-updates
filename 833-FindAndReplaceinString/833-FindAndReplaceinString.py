# Last updated: 8/4/2026, 12:43:05 PM
1class Solution:
2    def findReplaceString(self, s, indices, sources, targets):
3        original = s
4        valid = []
5        for i in range(len(indices)):
6            idx = indices[i]
7            if original.startswith(sources[i], idx):
8                valid.append(i)
9        for i in range(len(valid)):
10            for j in range(i + 1, len(valid)):
11                if indices[valid[i]] < indices[valid[j]]:
12                    valid[i], valid[j] = valid[j], valid[i]
13        for i in valid:
14            idx = indices[i]
15            s = s[:idx] + targets[i] + s[idx + len(sources[i]):]
16        return s