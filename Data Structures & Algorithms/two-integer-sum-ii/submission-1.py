class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers)
        while first <len(numbers):
            b =numbers[first]+numbers[second-1]
            match b:
                case b if b > target:
                    second-=1
                case b if b < target:
                    first+=1
                case b if b == target:
                    return [first+1,second]
                case _:
                    pass