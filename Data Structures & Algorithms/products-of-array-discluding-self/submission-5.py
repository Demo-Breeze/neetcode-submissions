import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer = [1]*n
        preceding = 1
        succeeding = 1
        for i in range(n):
            answer[i] = preceding
            preceding *= nums[i]
        for i in range(n-1,-1,-1):
            answer[i] *= succeeding 
            succeeding *= nums[i]
        return answer