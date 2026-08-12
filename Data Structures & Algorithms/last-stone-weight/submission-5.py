class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x= 0
        y=1
        
        while len(stones) > 1:
            stones.sort(reverse=True)
            if len(stones) == 2:
                return abs(stones[0]-stones[1])
            elif stones[0] == stones[1] and len(stones)>2:
                stones.pop(1)
                stones.pop(0)
            elif stones[0]< stones[1] or stones[0]>stones[1]:
                b=(stones[1]-stones[0])
                stones.pop(1)
                stones.pop(0)
                stones.append(abs(b))
            elif stones==[]:
                break
            else:
               print( "I did something wrong")
            print(stones)
        if len(stones)== 1:
            return stones[0]
        return stones
