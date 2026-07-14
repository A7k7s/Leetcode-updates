# Last updated: 7/14/2026, 2:02:32 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        n=set(nums)
        for i in range(1,len(nums)+1):
            if i not in n:
                res.append(i)
        return res

