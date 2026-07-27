# Last updated: 7/27/2026, 10:15:57 AM
1class Solution:
2    def maxDistance(self, arrays: List[List[int]]) -> int:
3        s=arrays[0][0]
4        b=arrays[0][-1]
5        mx=0
6        for i in range(1,len(arrays)):
7            arr=arrays[i]
8            mx=max(mx,abs(arr[0]-b),abs(arr[-1]-s))
9            s=min(arr[0],s)
10            b=max(arr[-1],b) 
11        return mx       