# Last updated: 8/28/2026, 11:12:18 AM
1class Solution:
2    def maxPoints(self, points: List[List[int]]) -> int:
3        if len(points) <= 2:
4            return len(points)
5        
6        def find_slope(p1, p2):
7            x1, y1 = p1
8            x2, y2 = p2
9            if x1-x2 == 0:
10                return inf
11            return (y1-y2)/(x1-x2)
12        
13        ans = 1
14        for i, p1 in enumerate(points):
15            slopes = defaultdict(int)
16            for j, p2 in enumerate(points[i+1:]):
17                slope = find_slope(p1, p2)
18                slopes[slope] += 1
19                ans = max(slopes[slope], ans)
20        return ans+1