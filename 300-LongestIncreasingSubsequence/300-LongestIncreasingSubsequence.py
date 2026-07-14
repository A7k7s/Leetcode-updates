# Last updated: 7/14/2026, 2:03:12 PM
class Solution:
    def lengthOfLIS(self, nums):
        res = []

        def binary_search(res, n):
            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        
        return len(res)