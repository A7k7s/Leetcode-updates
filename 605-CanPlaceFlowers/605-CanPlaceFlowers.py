# Last updated: 7/14/2026, 2:02:01 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        l = len(flowerbed)
        while i < l:
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == l - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  
                    count += 1
            i += 1
        return count >= n


        