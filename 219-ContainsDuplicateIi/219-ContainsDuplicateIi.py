# Last updated: 7/14/2026, 2:03:49 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        imap={}
        for i,num in enumerate(nums):
            if num in imap:
                if i-imap[num]<=k:
                    return True
            imap[num]=i
        return False