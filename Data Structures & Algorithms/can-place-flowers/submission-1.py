class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        final = []
        i = 0
        
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                final.append(1)
            else:
                prev_is_zero = (i == 0 or flowerbed[i - 1] == 0)
                next_is_zero = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if prev_is_zero and next_is_zero and n > 0:
                    final.append(1)
                    flowerbed[i] = 1
                    n -= 1
                else:
                    final.append(0)
            i += 1
            
        if n == 0:
            return True
        else:
            return False
