# Last updated: 7/14/2026, 2:06:18 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        m=0
        right=len(height)-1
        while(left<right):
            w=right-left
            h=min(height[left],height[right])
            a=w*h
            m=max(a,m)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
        return m
