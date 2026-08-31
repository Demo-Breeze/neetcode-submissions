class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers)
        while first <len(numbers):
            b =numbers[first]+numbers[second-1]
            if b > target:
                second-=1
            elif b < target:
                first+=1
            elif b == target:
                return [first+1,second]