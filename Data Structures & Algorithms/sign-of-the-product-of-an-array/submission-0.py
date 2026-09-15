import math
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        d = math.prod(nums)
        match d:
            case _ if d > 0:
                return 1
            case _ if d <0:
                return -1
            case 0:
                return 0
            case _:
                return "Not Compatible"